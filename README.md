# Django Blog Application

Welcome to the Django Blog Application! This is a feature-rich blogging platform built using Django, with various functionalities such as authentication, CRUD operations, post management (publishing, drafting, archiving), commenting, replying, and integration with Celery, Celery Beat, Flower, Redis, and Nginx.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

1. **Authentication:** User authentication is integrated into the application, allowing users to sign up, log in, and manage their profiles.

2. **CRUD Operations:** Perform Create, Read, Update, and Delete operations on blog posts, allowing users to manage their content efficiently.

3. **Post Management:**

   - **Publishing:** Users can publish blog posts to make them visible to the public.
   - **Drafting:** Save posts as drafts for later editing and publishing.
   - **Archiving:** Archive posts to keep them accessible while not being actively displayed.

4. **Comments and Replies:** Engage with readers through comments on blog posts. Users can also reply to comments for interactive discussions.

5. **Celery Integration:** Asynchronous task processing using Celery for improved performance and scalability.

6. **Celery Beat:** Schedule periodic tasks with Celery Beat to automate recurring actions, such as publishing scheduled posts.

7. **Flower Monitoring:** Monitor Celery tasks in real-time with Flower, providing insights into task execution and system health.

8. **Redis Integration:** Utilize Redis for caching and improving the performance of the application.

9. **Nginx Integration:** Deploy the application with Nginx as a reverse proxy server for improved security and performance.

## Requirements

Ensure your system meets the following requirements before installing the application:

- Python 3.x
- Django
- Celery
- Redis
- Nginx
- Flower

## Installation

1. Clone the repository:

```bash
    git clone https://github.com/faresemad/Blog.git
```

2. Build the application:

```bash
    make build
```

## Usage

1. Run the application:

```bash
    make up
```

2. Run the application in detached mode:

```bash
    make up-detached
```

## Configuration

The application can be configured by modifying the following files:

1. Configure Django settings in `blog/config/settings/base.py`.

2. Configure (Celery / Celery Beat / Flower) settings in `blog/config/celery.py` or `blog/compose/django/celery/(beat/flower/worker)`.

3. Configure Nginx settings in `blog/compose/nginx/nginx.conf`.

4. Configure Django Environment settings in `blog/.envs/.django`.

5. Configure Postgres Environment settings in `blog/.envs/.postgres`.

## Folder Structure

The application is structured as follows:

- **\`.envs\`** - Environment variable files for Django and Postgres.
- **\`apps\`** - Application-specific files.
- **\`config\`** - Settings for the application
- **\`compose\`** - Docker Compose configuration files.
- **\`requirements\`** - Application requirements files.
- **\`manage.py\`** - Django's command-line utility for administrative tasks.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
