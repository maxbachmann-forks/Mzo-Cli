# Monzo Cli
A (third-party) command line interface to your monzo account.

_Sometimes_ the command line is more convient then swiping and tapping.

The full monzo API isn't availible yet but the plan is to let easy
payments via the command line.

- Same auth as 1Password cli
- XOR store refresh token

### Command Examples
```fish
# monzo pay <name>... <amount> [--daily|--weekly|--monthly|--yearly|--every <x> (days|weeks|months|years) [--from (monday|tuesday|wednesday|thursday|friday|saturday|sunday)] [--sort-code <code> --account-number <number>]] [--message <message>]

$ monzo pay john 50.40

$ monzo pay patrick selman 30

$ monzo pay james 5 --weekly --from tomorrow

$ monzo pay vlad 2 --every 4 days --from friday

$ monzo pay dash 5 --sort-code 40-01-03 --account-number 123456789 --message "give it back"
```


### Credentials File
Access tokens held in memory (enviroment varaibles)
```toml
[default]
refresh_token_xor = "xxxxxxxxxxxx"
refresh_token_xor_verification = "xxxxxxxxxx"
```

### Config File
```toml
[default]
account_id = "xxxxxxxxxxx"
output_format = "<user|json>"
```
