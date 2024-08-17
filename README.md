# Bot Factory Purge Messages

## Overview

The Bot Factory Purge Messages bot is a Discord bot designed to help manage and clean up message history in a channel. With the `!purge` command, users with the appropriate permissions can delete a specified number of messages from the channel.

## Features

- **Purge Messages**: Allows users to delete up to 89 messages at a time.
- **Permissions Check**: Ensures that only users with the `Manage Messages` permission can use the command.
- **Error Handling**: Provides feedback for invalid inputs or permission issues.

## Command Usage

### `!purge <number>`

Deletes the last `<number>` of messages in the channel. The number must be greater than 0 and less than or equal to 89.

#### Examples

- To delete 10 messages:
  ```plaintext
  !purge 10
  ```

- To delete 50 messages:
  ```plaintext
  !purge 50
  ```

- To delete the maximum allowed number of messages (89):
  ```plaintext
  !purge 89
  ```

## Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/CalestialAshley35/Bot-Factory-Purger.git
   ```

2. **Install Dependencies**
   Navigate to the project directory and install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Add Your Bot Token**
   Replace `'your-bot-token'` in the `bot.run('your-bot-token')` line of the code with your actual Discord bot token.

4. **Run the Bot**
   ```bash
   python bot.py
   ```

## Project Link

You can view and interact with the Bot Factory Purge Messages bot here: [Replit Project](https://replit.com/@calestialashley/Bot-Factory-Purge-Messages?s=app)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please contact Calestial Ashley at calestialashley@gmail.com
