
# Reinforcement Learning Project

This repository contains various implementations of Reinforcement Learning algorithms applied to different environments and problems, such as ad optimization, CartPole balancing, Frozen Lake navigation, and Mountain Car challenge.

## Project Structure

- **Ads_Optimization Reinforcement**: A reinforcement learning approach to optimize ads selection.
  - `Ads_CTR_Optimisation.csv`: Dataset for ad click-through rate (CTR) optimization.
  - `Reinforcement Learning.py`: Python script for training and testing the ad optimization model.

- **Cartpole_Reinforcement Learning**: Solving the CartPole environment using Deep Q-Networks (DQN).
  - `CartPole_solved_DQN.ipynb`: Jupyter notebook implementing DQN to solve the CartPole environment.
  - `Cartpole_weights.h5`: Model weights file for CartPole DQN.
  - `TrainedModelCartpole.h5`: Trained model for CartPole.

- **FrozenLakeWithQLearning**: Implementation of Q-Learning to solve the Frozen Lake environment.
  - `Frozen_Lake_Q-Learning.ipynb`: Jupyter notebook applying Q-Learning to Frozen Lake.

- **MountainCar_Reinforcement Learning**: Solving the Mountain Car environment using Q-Learning and DQN.
  - `MountainCar(DQN).ipynb`: Jupyter notebook implementing DQN for the Mountain Car environment.
  - `Q_Learning_Mountain car.ipynb`: Jupyter notebook using Q-Learning for Mountain Car.
  - `TrainedModelMountainCar.h5`: Trained DQN model for Mountain Car.
  - `TrainedModelMountainCar_weights`: Weights file for the Mountain Car DQN model.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/reinforcement-learning-project.git
   ```

2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

You can run the provided Jupyter notebooks or Python scripts to train models or load the pre-trained models provided in the repository.

Example of running the CartPole DQN model:
```bash
python CartPole_solved_DQN.py
```

## Contributing

Feel free to submit pull requests for improvements or bug fixes. Contributions are welcome!

