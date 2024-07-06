# This is the main file for an advantage actor critic (A2C) algorithm.
# The agent random sample a batch in the replay buffer, and optimize the policy gradient and value function loss.
# This can be a first RL algorithm code for the starters.
import torch
from argparse import Namespace
from xuance.environment import DummyVecEnv
from xuance.torch.utils import NormalizeFunctions, ActivationFunctions
from xuance.torch.policies import REGISTRY_Policy
from xuance.torch.agents import OnPolicyAgent


class A2C_Agent(OnPolicyAgent):
    """The implementation of A2C agent.

    Args:
        config: the Namespace variable that provides hyper-parameters and other settings.
        envs: the vectorized environments.
    """

    def __init__(self,
                 config: Namespace,
                 envs: DummyVecEnv):
        super(A2C_Agent, self).__init__(config, envs)
        # Build memory.
        self.memory = self._build_memory()

        # Build policy.
        self.policy = self._build_policy()

        # Build optimizer.
        optimizer = torch.optim.Adam(self.policy.parameters(), self.config.learning_rate, eps=1e-5)

        # Build learning rate scheduler.
        lr_scheduler = torch.optim.lr_scheduler.LinearLR(optimizer, start_factor=1.0, end_factor=0.0,
                                                         total_iters=self.config.running_steps)
        # Build learner.
        self.learner = self._build_learner(self.config, envs.max_episode_steps, self.policy, optimizer, lr_scheduler)

    def _build_policy(self):
        normalize_fn = NormalizeFunctions[self.config.normalize] if hasattr(self.config, "normalize") else None
        initializer = torch.nn.init.orthogonal_
        activation = ActivationFunctions[self.config.activation]
        device = self.device

        # build representation.
        representation = self._build_representation(self.config.representation, self.observation_space, self.config)

        # build policy.
        if self.config.policy == "Categorical_AC":
            policy = REGISTRY_Policy["Categorical_AC"](
                action_space=self.action_space, representation=representation,
                actor_hidden_size=self.config.actor_hidden_size, critic_hidden_size=self.config.critic_hidden_size,
                normalize=normalize_fn, initialize=initializer, activation=activation, device=device)
        elif self.config.policy == "Gaussian_AC":
            policy = REGISTRY_Policy["Gaussian_AC"](
                action_space=self.action_space, representation=representation,
                actor_hidden_size=self.config.actor_hidden_size, critic_hidden_size=self.config.critic_hidden_size,
                normalize=normalize_fn, initialize=initializer, activation=activation, device=device,
                activation_action=ActivationFunctions[self.config.activation_action])
        else:
            raise AttributeError(f"A2C currently does not support the policy named {self.config.policy}.")

        return policy
