# ewokswhale: a Docker application to edit, manage and execute Ewoks workflows 🐳

## Quick start 🚀

- Copy your workflows in `resources/workflows`
- Run `docker-compose up`
- Access the app at `http://localhost:8000`

Workflows/tasks changes will be propagated to the `resources` folder.

## Repository contents 📦

ewokswhale provides Docker images to run a fullstack application to run [ewoksweb](https://ewoksweb.readthedocs.io) in a web browser and execute workflows in a worker.

The complete set-up is composed for three containers:

- The fullstack application [ewoksweb](https://ewoksweb.readthedocs.io)
- An Ewoks worker started by [ewoksjob](https://ewoksjob.readthedocs.io/en/latest/)]
- A [Redis](https://redis.io/) server to handle communications between ewoksweb and the worker

The full application can be run with `docker-compose`:

```
docker-compose up
```

Ewoksweb can be accessed at `http://localhost:8000/edit`. A workflow can be specified by the query param `workflow`. Ex: `demo` can be opened by accessing `http://localhost:8000/edit?workflow=demo`.

The value of the port (default: `8000`) can be changed in the `.env` file. The value of the port used for the redis-server can also be changed the same way.
