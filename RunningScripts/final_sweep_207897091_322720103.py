import wandb
YOUR_WANDB_USERNAME = "noa-levi"
project = "NLP2024_PROJECT_207897091_322720103"

command = [
        "${ENVIRONMENT_VARIABLE}",
        "${interpreter}",
        "StrategyTransfer.py",
        "${project}",
        "${args}"
    ]

sweep_config_1 = {
    "name": "decide between relaxed strategies",
    "method": "grid",
    "metric": {
        "goal": "maximize",
        "name": "AUC.test.max"
    },
    "parameters": {
        "ENV_HPT_mode": {"values": [True]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [0, 4]},
        #"features": {"values": ["EFs", "GPT4", "BERT"]},
        "basic_nature": {"values": [17,18,19,20,21,22,23,24]},
    },
    "command": command
}

sweep_config_0 = {
    "name": "initialize",
    "method": "grid",
    "parameters": {
        "ENV_HPT_mode": {"values": [True]},
        "seed": {"values": list(range(1, 6))},
        "basic_nature": {"values": [17,18,19,20,21,22,23,24]},
    },
    "command": command
}
sweep_config = {
    "name": "TRYING TO FIX THE BUGS",
    "method": "grid",
    "metric": {
        "goal": "maximize",
        "name": "AUC.test.max"
    },
    "parameters": {
        "ENV_HPT_mode": {"values": [False]},
        "seed": {"values": list(range(1, 6))},
    },
    "command": command
}

sweep_config_00 = {
    "name": "TRYING TO FIX THE BUGS",
    "method": "grid",
    "parameters": {
        "ENV_HPT_mode": {"values": [True]},
        "seed": {"values": list(range(1, 6))},
    },
    "command": command
}

# sweep_id = wandb.sweep(sweep=sweep_config, project=project)
# print("run this line to run your agent in a screen:")
# print(f"screen -dmS \"sweep_agent\" wandb agent {YOUR_WANDB_USERNAME}/{project}/{sweep_id}")

sweep_id = wandb.sweep(sweep=sweep_config_0, project=project)
print("run this line to run your agent in a screen:")
print(f"screen -dmS \"sweep_agent\" wandb agent {YOUR_WANDB_USERNAME}/{project}/{sweep_id}")

# sweep_id = wandb.sweep(sweep=sweep_config_0, project=project)
# print("run this line to run your agent in a screen:")
# print(f"screen -dmS \"sweep_agent\" wandb agent {YOUR_WANDB_USERNAME}/{project}/{sweep_id}")
