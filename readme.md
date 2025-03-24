# HourAHour

HourAHour is a project developed to record weather conditions hourly, allowing you to set a region, state, and country.

## Features

The project includes the following features:

- Retrieves real-time weather information for Blumenau, SC, using the wttr.in service.
- Creates and updates a text file with weather details, execution time, and location.
- Performs automatic commits to a Git repository every hour and daily at 08:00.
- Logs detailed records of each operation in a `commit_diario.log` file.
- Handles errors during execution, logging messages for later analysis.

## Technologies Useds

The project was developed using the following technologies:

- **Python**: Primary programming language for the project.
- **wttr.in**: Weather API to fetch meteorological information for Blumenau.
- **schedule**: Library for scheduling recurring tasks.
- **subprocess**: Used for integrating with Git commands.
- **requests**: Library for making HTTP calls to the weather API.
- **unittest**: Python library focused on unit testing.

## Key Learnings

Key takeaways from this project include:

- Automating Git contributions to reduce the need for manual actions.
- Using public APIs to fetch external information (such as weather) and integrating it into workflows.
- Configuring and managing recurring tasks using the `schedule` library.
- Logging events and error messages in persistent logs to facilitate debugging and analysis.
- Applying Python coding best practices, including handling encoding to avoid issues with Unicode characters.

## Conclusion

HourAHour is a practical tool for automating the creation of commits in a Git repository, recording real-time weather information. The project highlights important concepts such as automation, API integration, log management, and task scheduling, providing an efficient and reliable solution to maintain an up-to-date Git history.
