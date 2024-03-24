import { createServer, Model } from 'miragejs';

const DEFAULT_CONFIG = {
    environment: "development",
    namespace: "api",
};


function wrap_response(code, message, data){
    return {
        status_code: code,
        message: message,
        data: data
    }
}

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
            this.post('/todos', (schema, request) => {
                let attrs = JSON.parse(request.requestBody);
                return schema.todos.create(attrs);
            });
            this.post('/auth/login', (schema, request) => {
                let jsonData = JSON.parse(request.requestBody);
                if (jsonData.username === 'guest1' && jsonData.password === 'guest1') {
                    return JSON.stringify(wrap_response(200, "Login successful", {
                        access_token: "1234567890",
                    }));
                }else{
                    return JSON.stringify(wrap_response(401, "Invalid credentials", {}));
                }
            });
            
        }
    });

    return server;
}

