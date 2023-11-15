from typing import Sequence, Callable, Tuple, Optional

import torch
from torch import nn

import numpy as np

import cs285.infrastructure.pytorch_util as ptu
from cs285.agents.dqn_agent import DQNAgent


class CQLAgent(DQNAgent):
    def __init__(
        self,
        observation_shape: Sequence[int],
        num_actions: int,
        cql_alpha: float,
        cql_temperature: float = 1.0,
        **kwargs,
    ):
        super().__init__(
            observation_shape=observation_shape, num_actions=num_actions, **kwargs
        )
        self.cql_alpha = cql_alpha
        self.cql_temperature = cql_temperature

    def compute_critic_loss(
        self,
        obs: torch.Tensor,
        action: torch.Tensor,
        reward: torch.Tensor,
        next_obs: torch.Tensor,
        done: bool,
    ) -> Tuple[torch.Tensor, dict, dict]:

        loss, metrics, variables = super().compute_critic_loss(
            obs,
            action,
            reward,
            next_obs,
            done,
        )

        # TODO(student): modify the loss to implement CQL
        # Hint: `variables` includes qa_values and q_values from your CQL implementation
        # loss = loss + ...

        qa_values = variables['qa_values']

        # Compute CQL term
        random_actions = torch.randint(0, self.num_actions, action.shape, device=action.device)
        random_q_values = self.critic(obs).gather(1, random_actions.unsqueeze(1)).squeeze(1)

        # Calculate CQL loss
        cql_loss = self.cql_alpha * (qa_values.logsumexp(dim=1) - random_q_values.mean()).mean()

        # Add CQL loss to the original DQN loss
        loss = loss + cql_loss


        return loss, metrics, variables

    def update_target_critic(self):
        """
        Update the target critic network by copying weights from the main critic network.
        """
        self.target_critic.load_state_dict(self.critic.state_dict())

    def update(
            self,
            obs: torch.Tensor,
            action: torch.Tensor,
            reward: torch.Tensor,
            next_obs: torch.Tensor,
            done: torch.Tensor,
            step: int,
    ) -> dict:
        """Update the agent's network."""
        # Update the critic
        critic_loss, critic_metrics, critic_variables = self.compute_critic_loss(
            obs,
            action,
            reward,
            next_obs,
            done,
        )
        self.critic_optimizer.zero_grad()
        critic_loss.backward()
        self.critic_optimizer.step()

        if step % self.target_update_period == 0:
            self.update_target_critic()

        # Return the loss and any extra metrics
        metrics = {
            **critic_metrics,
        }
        return metrics