import wandb
YOUR_WANDB_USERNAME = "noa7566"
<<<<<<< HEAD:RunningScripts/final_sweep_YOUR_UID.py
project = "NLP2024_PROJECT_YOUR_UID"
=======
project = "NLP2024_PROJECT_207897091_322720103"
>>>>>>> 3c771de1e42ce9267a93ffc83ebc30795cba6694:RunningScripts/first_try_sweep.py

command = [
        "${ENVIRONMENT_VARIABLE}",
        "${interpreter}",
        "StrategyTransfer.py",
        "${project}",
        "${args}"
    ]

sweep_config_1 = {
    "name": "LSTM: SimFactor=0/4 for any features representation",
    "method": "grid",
    "metric": {
        "goal": "maximize",
        "name": "AUC.test.max"
    },
    "parameters": {
        "ENV_HPT_mode": {"values": [False]},
        "architecture": {"values": ["LSTM"]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [0, 4]},
        "features": {"values": ["EFs", "GPT4", "BERT"]},
<<<<<<< HEAD:RunningScripts/final_sweep_YOUR_UID.py
        #"basic_nature": {"values": [18,19,20]},
=======
        "basic_nature": {"values": [18,19,20]},
>>>>>>> 3c771de1e42ce9267a93ffc83ebc30795cba6694:RunningScripts/first_try_sweep.py
    },
    "command": command
}

# Initialize a new sweep
sweep_id = wandb.sweep(sweep=sweep_config_1, project=project)
print("run this line to run your agent in a screen:")
print(f"screen -dmS \"sweep_agent\" wandb agent {YOUR_WANDB_USERNAME}/{project}/{sweep_id}")
