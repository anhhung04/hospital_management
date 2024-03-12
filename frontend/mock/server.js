import { createServer, Model } from 'miragejs';

const DEFAULT_CONFIG = {
    environment: "development",
    namespace: "api",
};

export function makeServer({ environment, namespace } =
    DEFAULT_CONFIG) {
    let server = createServer({
        environment,
        namespace,
        models: {
            Todo: Model,
        }, routes() {
            this.namespace = 'api/';
            this.get('/demo/hello', (schema, request) => {
                return {
                    message: "Hello user with cred: " + request.requestHeaders.Authorization
                };
            });
        }
    });

    return server;
}

