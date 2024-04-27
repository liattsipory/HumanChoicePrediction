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
sweep_config_1_no_metric = {
    "name": "decide between relaxed strategies",
    "method": "grid",
    "parameters": {
        "ENV_HPT_mode": {"values": [True]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [0, 4]},
        #"features": {"values": ["EFs", "GPT4", "BERT"]},
        "basic_nature": {"values": [17,18,19,20,21,22,23,24]},
    },
    "command": command
}
sweep_config_2_no_metric = {
    "name": "decide between unrelaxed first and last new astrengies",
    "method": "grid",
    "parameters": {
        "ENV_HPT_mode": {"values": [True]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [0, 4]},
        #"features": {"values": ["EFs", "GPT4", "BERT"]},
        "basic_nature": {"values": [25,26,27,28]},
    },
    "command": command
}
sweep_config_3_with_metric_all = {
    "name": "decide between all new astrengies with metric",
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
        "basic_nature": {"values": [17,18,19,20,21,22,23,24,25,26,27,28]},
    },
    "command": command
}
sweep_config_3_no_metric_all = {
    "name": "decide between all new astrengies",
    "method": "grid",
    "parameters": {
        "ENV_HPT_mode": {"values": [True]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [0, 4]},
        #"features": {"values": ["EFs", "GPT4", "BERT"]},
        "basic_nature": {"values": [17,18,19,20,21,22,23,24,25,26,27,28]},
    },
    "command": command
}
# sweep_config_0 = {
#     "name": "initialize",
#     "method": "grid",
#     "parameters": {
#         "ENV_HPT_mode": {"values": [True]},
#         "seed": {"values": list(range(1, 6))},
#         "basic_nature": {"values": [17,18,19,20,21,22,23,24]},
#     },
#     "command": command
# }
# sweep_config = {
#     "name": "TRYING TO FIX THE BUGS",
#     "method": "grid",
#     "metric": {
#         "goal": "maximize",
#         "name": "AUC.test.max"
#     },
#     "parameters": {
#         "ENV_HPT_mode": {"values": [False]},
#         "seed": {"values": list(range(1, 6))},
#     },
#     "command": command
# }

# sweep_config_00 = {
#     "name": "TRYING TO FIX THE BUGS",
#     "method": "grid",
#     "parameters": {
#         "ENV_HPT_mode": {"values": [True]},
#         "seed": {"values": list(range(1, 6))},
#     },
#     "command": command
# }

# sweep_id = wandb.sweep(sweep=sweep_config, project=project)
# print("run this line to run your agent in a screen:")
# print(f"screen -dmS \"sweep_agent\" wandb agent {YOUR_WANDB_USERNAME}/{project}/{sweep_id}")

sweep_id = wandb.sweep(sweep=sweep_config_3_with_metric_all, project=project)
print("run this line to run your agent in a screen:")
print(f"screen -dmS \"sweep_agent\" wandb agent {YOUR_WANDB_USERNAME}/{project}/{sweep_id}")

# sweep_id = wandb.sweep(sweep=sweep_config_0, project=project)
# print("run this line to run your agent in a screen:")
# print(f"screen -dmS \"sweep_agent\" wandb agent {YOUR_WANDB_USERNAME}/{project}/{sweep_id}")
