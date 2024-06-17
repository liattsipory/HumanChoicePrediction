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

#--------------------------------------------------------------------------------------------
#what we actually ran:
sweep_config_validation_choose_relaxed = {
    "name": "choose relaxed  strategies after check on valset - 17, 18, 19, 20, 21, 22, 23, 24",
    "method": "grid",
    "parameters": {
        "ENV_HPT_mode": {"values": [True]},
        "architecture": {"values": ["LSTM"]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [4]},
        #"features": {"values": ["EFs", "GPT4", "BERT"]},
        "basic_nature": {"values": [17, 18, 19, 20, 21, 22, 23,24]},
    },
    "command": command
}
sweep_config_validation_basic_12 = {
    "name": "try basic config with basic nature= 12 on validation set",
    "method": "grid",
    "parameters": {
        "ENV_HPT_mode": {"values": [True]},
        "architecture": {"values": ["LSTM"]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [4]},
        #"features": {"values": ["EFs", "GPT4", "BERT"]},
        "basic_nature": {"values": [17, 18, 19, 20, 21, 22, 23,24]},
    },
    "command": command
}
sweep_config_test_first = {
    "name": "run relaxed stradegies on test set [21, 30, 34]",
    "method": "grid",
    "parameters": {
        "ENV_HPT_mode": {"values": [False]},
        "architecture": {"values": ["LSTM"]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [4]},
        #"features": {"values": ["EFs", "GPT4", "BERT"]},
        "basic_nature": {"values": [21, 30, 34]},
    },
    "command": command
}
sweep_config_test_second = {
    "name": "run relaxed stradegies on test set [12, 26, 27, 28, 32, 33]",
    "method": "grid",
    "parameters": {
        "ENV_HPT_mode": {"values": [False]},
        "architecture": {"values": ["LSTM"]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [4]},
        #"features": {"values": ["EFs", "GPT4", "BERT"]},
        "basic_nature": {"values": [12, 26, 27, 28, 32, 33]},
    },
    "command": command
}
sweep_config_test_third = {
    "name": "run unrelaxed stradegies on test set [29, 20, 31, 32, 33]",
    "method": "grid",
    "parameters": {
        "ENV_HPT_mode": {"values": [False]},
        "architecture": {"values": ["LSTM"]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [4]},
        #"features": {"values": ["EFs", "GPT4", "BERT"]},
        "basic_nature": {"values": [29, 20, 31, 32, 33]},
    },
    "command": command
}
sweep_config_test_last = {
    "name": "run  stradegies on test set [12, 24, 25, 26, 27, 28]",
    "method": "grid",
    "parameters": {
        "ENV_HPT_mode": {"values": [False]},
        "architecture": {"values": ["LSTM"]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [4]},
        #"features": {"values": ["EFs", "GPT4", "BERT"]},
        "basic_nature": {"values": [12, 24, 25, 26, 27, 28]},
    },
    "command": command
}

#--------------------------------------------------------------------------------------------
#what you need to run without duplicates:
sweep_config_validation = {
    "name": "choose relaxed  strategies after check on valset - 12, 17, 18, 19, 20, 21, 22, 23, 24",
    "method": "grid",
    "parameters": {
        "ENV_HPT_mode": {"values": [True]},
        "architecture": {"values": ["LSTM"]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [4]},
        #"features": {"values": ["EFs", "GPT4", "BERT"]},
        "basic_nature": {"values": [12, 17, 18, 19, 20, 21, 22, 23,24]},
    },
    "command": command
}
sweep_config_test = {
    "name": "run  stradegies on test set [12, 20, 21, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]",
    "method": "grid",
    "parameters": {
        "ENV_HPT_mode": {"values": [False]},
        "architecture": {"values": ["LSTM"]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [4]},
        #"features": {"values": ["EFs", "GPT4", "BERT"]},
        "basic_nature": {"values": [12, 20, 21, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]},
    },
    "command": command
}

sweep_id = wandb.sweep(sweep=sweep_config_validation, project=project)
print("run this line to run your agent in a screen:")
print(f"screen -dmS \"sweep_agent\" wandb agent {YOUR_WANDB_USERNAME}/{project}/{sweep_id}")
sweep_id = wandb.sweep(sweep=sweep_config_test, project=project)
print("run this line to run your agent in a screen:")
print(f"screen -dmS \"sweep_agent\" wandb agent {YOUR_WANDB_USERNAME}/{project}/{sweep_id}")

