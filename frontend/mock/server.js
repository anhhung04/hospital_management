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
            this.post('/auth/verify', (schema, request) => {
                let jsonData = JSON.parse(request.requestBody);
                if (jsonData.access_token === '1234567890') {
                    return JSON.stringify(
                        {
                            "status_code": 200,
                            "message": "Login successful",
                            "data": {
                                "isLogin": true,
                                "username": "guest1",
                                "user_id": 1,
                            }
                        }
                    );
                }else{
                    return JSON.stringify(wrap_response(401, "Invalid credentials", {}));
                }
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
            this.get('/patients/list', () => {
                return [
                        {
                            id: 1,
                            name: "Nguyễn Văn A",
                            phone: "0123456789",
                            date: "01/01/2022",
                            time: "10:00 AM",
                            detail: "Hồ sơ ↗",
                        },
                        {
                            id: 2,
                            name: "Nguyễn Văn A",
                            phone: "0123456789",
                            date: "01/01/2022",
                            time: "10:00 AM",
                            detail: "Hồ sơ ↗",
                        },
                        {
                            id: 3,
                            name: "Nguyễn Văn A",
                            phone: "0123456789",
                            date: "01/01/2022",
                            time: "10:00 AM",
                            detail: "Hồ sơ ↗",
                        },
                        {
                            id: 4,
                            name: "Nguyễn Văn A",
                            phone: "0123456789",
                            date: "01/01/2022",
                            time: "10:00 AM",
                            detail: "Hồ sơ ↗",
                        },
                        {
                            id: 5,
                            name: "Nguyễn Văn A",
                            phone: "0123456789",
                            date: "01/01/2022",
                            time: "10:00 AM",
                            detail: "Hồ sơ ↗",
                        },
                        {
                            id: 6,
                            name: "Nguyễn Văn A",
                            phone: "0123456789",
                            date: "01/01/2022",
                            time: "10:00 AM",
                            detail: "Hồ sơ ↗",
                        },
                        {
                            id: 7,
                            name: "Nguyễn Văn A",
                            phone: "0123456789",
                            date: "01/01/2022",
                            time: "10:00 AM",
                            detail: "Hồ sơ ↗",
                        },
                        {
                            id: 8,
                            name: "Nguyễn Văn A",
                            phone: "0123456789",
                            date: "01/01/2022",
                            time: "10:00 AM",
                            detail: "Hồ sơ ↗",
                        },
                        {
                            id: 9,
                            name: "Nguyễn Văn A",
                            phone: "0123456789",
                            date: "01/01/2022",
                            time: "10:00 AM",
                            detail: "Hồ sơ ↗",
                        },
                        {
                            id: 10,
                            name: "Nguyễn Văn A",
                            phone: "0123456789",
                            date: "01/01/2022",
                            time: "10:00 AM",
                            detail: "Hồ sơ ↗",
                        },
                        {
                            id: 11,
                            name: "Nguyễn Văn A",
                            phone: "0123456789",
                            date: "01/01/2022",
                            time: "10:00 AM",
                            detail: "Hồ sơ ↗",
                        },
                        {
                            id: 12,
                            name: "Nguyễn Văn A",
                            phone: "0123456789",
                            date: "01/01/2022",
                            time: "10:00 AM",
                            detail: "Hồ sơ ↗",
                        },
                        {
                            id: 13,
                            name: "Nguyễn Văn A",
                            phone: "0123456789",
                            date: "01/01/2022",
                            time: "10:00 AM",
                            detail: "Hồ sơ ↗",
                        }
                    ]
                
            });
            this.get('/generalinfo', () => {
                const general_info = [
                    {
                        title: "Bệnh nhân",
                        value: "1000",
                        path: "/patient",
                    },
                    {
                        title: "Nhân viên",
                        value: "50",
                        path: "/patient",
                    },
                    {
                        title: "Y tá",
                        value: "200",
                        path: "/patient",
                    },
                    {
                        title: "Bác sĩ",
                        value: "300",
                        path: "/patient",
                    },
                ];

                return general_info;
            });
            
        }
    });

    return server;
}

