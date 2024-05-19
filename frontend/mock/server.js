import { createServer, Model, Response } from "miragejs"

export function makeServer () {
  createServer({
    models: {
      employee: Model // Define the employees model
    },

    seeds(server) {
      server.create("employee", {
        id: 1,
        lastName: "Nguyễn Văn",
        firstName: "A",
        type: "Bác sĩ",
        faculty: "Thần kinh",
        status: "Khám bệnh",
        address: "268 Lý Thường Kiệt, Phường 14, Quận 10, TPHCM",
        dateBegin:  "2024-05-01",
        dateEnd: "2029-12-25",
        degree: ["bang bac si", "chung chi hanh nghe"],
        dob: "2004-08-23",
        email: "nhu.nguyenquynh0109@hcmut.edu.vn",
        gender: "Nữ",
        jobTitle: "Tiến sĩ",
        med: "0123456789",
        phone: "0123456789",
        position: "Trưởng khoa",
        ssn: "0123456789",
        scheduler: {
          "04/28/2024": [
            {
              id: 1,
              begin_time: "7:00 AM",
              end_time: "9:00 AM",
              frequency: "single"
            },
            {
              id: 2,
              begin_time: "9:00 AM",
              end_time: "11:00 AM",
              frequency: "single"
            }
          ],
          "04/29/2024": [
            {
              id: 1,
              begin_time: "7:00 AM",
              end_time: "9:00 AM",
              frequency: "single"
            },
            {
              id: 2,
              begin_time: "9:00 AM",
              end_time: "11:00 AM",
              frequency: "single"
            }
          ]
        }
    })

    // scheduler: [
    //   {
    //     inTime: "7:00 AM",
    //     outTime: "9:00 AM",
    //     date: "05/19/2024",
    //     it: "never" 
    //   },
    //   {
    //     inTime: "9:00 AM",
    //     outTime: "12:00 AM",
    //     date: "05/19/2024",
    //     it: "never" 
    //   },
    //   {
    //     inTime: "1:00 PM",
    //     outTime: "3:00 pM",
    //     date: "05/19/2024",
    //     it: "never" 
    //   },
    // ]
      server.create("employee", {
        id: 2,
        lastName: "Nguyễn Văn",
        firstName: "B",
        type: "Bác sĩ",
        faculty: "Tiêu hóa",
        status: "Trống",
        address: "268 Lý Thường Kiệt, Phường 14, Quận 10, TPHCM",
        dateBegin:  "2024-05-01",
        dateEnd: "2029-12-25",
        degree: [],
        dob: "2004-08-23",
        email: "nhu.nguyenquynh0109@hcmut.edu.vn",
        gender: "Nữ",
        jobTitle: "Tiến sĩ",
        med: "0123456789",
        phone: "0123456789",
        position: "Trưởng khoa",
        ssn: "0123456789",
        scheduler: {}
    })
      server.create("employee", {
        id: 3,
        lastName: "Nguyễn Văn",
        firstName: "C",
        type: "Bác sĩ",
        faculty: "Phụ sản",
        status: "Phẫu thuật",
        address: "268 Lý Thường Kiệt, Phường 14, Quận 10, TPHCM",
        dateBegin:  "2024-05-01",
        dateEnd: "2029-12-25",
        degree: [],
        dob: "2004-08-23",
        email: "nhu.nguyenquynh0109@hcmut.edu.vn",
        gender: "Nữ",
        jobTitle: "Tiến sĩ",
        med: "0123456789",
        phone: "0123456789",
        position: "Trưởng khoa",
        ssn: "0123456789",
        scheduler: {}
    })
      server.create("employee", {
        id: 4,
        lastName: "Nguyễn Văn",
        firstName: "D",
        type: "Bác sĩ",
        faculty: "Thần kinh",
        status: "Khám bệnh",
        address: "268 Lý Thường Kiệt, Phường 14, Quận 10, TPHCM",
        dateBegin:  "2024-05-01",
        dateEnd: "2029-12-25",
        degree: [],
        dob: "2004-08-23",
        email: "nhu.nguyenquynh0109@hcmut.edu.vn",
        gender: "Nữ",
        jobTitle: "Tiến sĩ",
        med: "0123456789",
        phone: "0123456789",
        position: "Trưởng khoa",
        ssn: "0123456789",
        scheduler: {}
    })
      server.create("employee", {
        id: 5,
        lastName: "Nguyễn Văn",
        firstName: "E",
        type: "Y tá",
        faculty: "Tiêu hóa",
        status: "Trống",
        address: "268 Lý Thường Kiệt, Phường 14, Quận 10, TPHCM",
        dateBegin:  "2024-05-01",
        dateEnd: "2029-12-25",
        degree: [],
        dob: "2004-08-23",
        email: "nhu.nguyenquynh0109@hcmut.edu.vn",
        gender: "Nữ",
        jobTitle: "Tiến sĩ",
        med: "0123456789",
        phone: "0123456789",
        position: "Trưởng khoa",
        ssn: "0123456789",
        scheduler: {}
    })
      server.create("employee", {
        id: 6,
        lastName: "Nguyễn Văn",
        firstName: "F",
        type: "Bác sĩ",
        faculty: "Phụ sản",
        status: "Phẫu thuật",
        address: "268 Lý Thường Kiệt, Phường 14, Quận 10, TPHCM",
        dateBegin:  "2024-05-01",
        dateEnd: "2029-12-25",
        degree: [],
        dob: "2004-08-23",
        email: "nhu.nguyenquynh0109@hcmut.edu.vn",
        gender: "Nữ",
        jobTitle: "Tiến sĩ",
        med: "0123456789",
        phone: "0123456789",
        position: "Trưởng khoa",
        ssn: "0123456789",
        scheduler: {}
    })
      server.create("employee", {
        id: 7,
        lastName: "Nguyễn Văn",
        firstName: "G",
        type: "Bác sĩ",
        faculty: "Thần kinh",
        status: "Khám bệnh",
        address: "268 Lý Thường Kiệt, Phường 14, Quận 10, TPHCM",
        dateBegin:  "2024-05-01",
        dateEnd: "2029-12-25",
        degree: [],
        dob: "2004-08-23",
        email: "nhu.nguyenquynh0109@hcmut.edu.vn",
        gender: "Nữ",
        jobTitle: "Tiến sĩ",
        med: "0123456789",
        phone: "0123456789",
        position: "Trưởng khoa",
        ssn: "0123456789",
        scheduler: {}
    })
      server.create("employee", {
        id: 8,
        lastName: "Nguyễn Văn",
        firstName: "H",
        type: "Y tá",
        faculty: "Tiêu hóa",
        status: "Trống",
        address: "268 Lý Thường Kiệt, Phường 14, Quận 10, TPHCM",
        dateBegin:  "2024-05-01",
        dateEnd: "2029-12-25",
        degree: [],
        dob: "2004-08-23",
        email: "nhu.nguyenquynh0109@hcmut.edu.vn",
        gender: "Nữ",
        jobTitle: "Tiến sĩ",
        med: "0123456789",
        phone: "0123456789",
        position: "Trưởng khoa",
        ssn: "0123456789",
        scheduler: {}
    })
      server.create("employee", {
        id: 9,
        lastName: "Nguyễn Văn",
        firstName: "I",
        type: "Bác sĩ",
        faculty: "Y tá",
        status: "Phẫu thuật",
        address: "268 Lý Thường Kiệt, Phường 14, Quận 10, TPHCM",
        dateBegin:  "2024-05-01",
        dateEnd: "2029-12-25",
        degree: [],
        dob: "2004-08-23",
        email: "nhu.nguyenquynh0109@hcmut.edu.vn",
        gender: "Nữ",
        jobTitle: "Tiến sĩ",
        med: "0123456789",
        phone: "0123456789",
        position: "Trưởng khoa",
        ssn: "0123456789",
        scheduler: {}
    })
      server.create("employee", {
        id: 10,
        nlastName: "Nguyễn Văn",
        firstName: "J",
        type: "Bác sĩ",
        faculty: "Thần kinh",
        status: "Khám bệnh",
        address: "268 Lý Thường Kiệt, Phường 14, Quận 10, TPHCM",
        dateBegin:  "2024-05-01",
        dateEnd: "2029-12-25",
        degree: [],
        dob: "2004-08-23",
        email: "nhu.nguyenquynh0109@hcmut.edu.vn",
        gender: "Nữ",
        jobTitle: "Tiến sĩ",
        med: "0123456789",
        phone: "0123456789",
        position: "Trưởng khoa",
        ssn: "0123456789",
        scheduler: {}
    })
      server.create("employee", {
        id: 11,
        lastName: "Nguyễn Văn",
        firstName: "K",
        type: "Bác sĩ",
        faculty: "Tiêu hóa",
        status: "Trống",
        address: "268 Lý Thường Kiệt, Phường 14, Quận 10, TPHCM",
        dateBegin:  "2024-05-01",
        dateEnd: "2029-12-25",
        degree: [],
        dob: "2004-08-23",
        email: "nhu.nguyenquynh0109@hcmut.edu.vn",
        gender: "Nữ",
        jobTitle: "Tiến sĩ",
        med: "0123456789",
        phone: "0123456789",
        position: "Trưởng khoa",
        ssn: "0123456789",
        scheduler: {}
    })
      server.create("employee", {
        id: 12,
        lastName: "Nguyễn Văn",
        firstName: "L",
        type: "Bác sĩ",
        faculty: "Phụ sản",
        status: "Phẫu thuật",
        address: "268 Lý Thường Kiệt, Phường 14, Quận 10, TPHCM",
        dateBegin:  "2024-05-01",
        dateEnd: "2029-12-25",
        degree: [],
        dob: "2004-08-23",
        email: "nhu.nguyenquynh0109@hcmut.edu.vn",
        gender: "Nữ",
        jobTitle: "Tiến sĩ",
        med: "0123456789",
        phone: "0123456789",
        position: "Trưởng khoa",
        ssn: "0123456789",
        scheduler: {}
    })
      server.create("employee", {
        id: 13,
        lastName: "Nguyễn Văn",
        firstName: "M",
        type: "Y tá",
        faculty: "Thần kinh",
        status: "Khám bệnh",
        address: "268 Lý Thường Kiệt, Phường 14, Quận 10, TPHCM",
        dateBegin:  "2024-05-01",
        dateEnd: "2029-12-25",
        degree: [],
        dob: "2004-08-23",
        email: "nhu.nguyenquynh0109@hcmut.edu.vn",
        gender: "Nữ",
        jobTitle: "Tiến sĩ",
        med: "0123456789",
        phone: "0123456789",
        position: "Trưởng khoa",
        ssn: "0123456789",
        scheduler: {}
    })
      server.create("employee", {
        id: 14,
        lastName: "Nguyễn Văn",
        firstName: "N",
        type: "Bác sĩ",
        faculty: "Tiêu hóa",
        status: "Trống",
        address: "268 Lý Thường Kiệt, Phường 14, Quận 10, TPHCM",
        dateBegin:  "2024-05-01",
        dateEnd: "2029-12-25",
        degree: [],
        dob: "2004-08-23",
        email: "nhu.nguyenquynh0109@hcmut.edu.vn",
        gender: "Nữ",
        jobTitle: "Tiến sĩ",
        med: "0123456789",
        phone: "0123456789",
        position: "Trưởng khoa",
        ssn: "0123456789",
        scheduler: {}
    })
      server.create("employee", {
        id: 15,
        lastName: "Nguyễn Văn",
        firstName: "O",
        type: "Khác",
        faculty: "Phụ sản",
        status: "Phẫu thuật",
        address: "268 Lý Thường Kiệt, Phường 14, Quận 10, TPHCM",
        dateBegin:  "2024-05-01",
        dateEnd: "2029-12-25",
        degree: [],
        dob: "2004-08-23",
        email: "nhu.nguyenquynh0109@hcmut.edu.vn",
        gender: "Nữ",
        jobTitle: "Tiến sĩ",
        med: "0123456789",
        phone: "0123456789",
        position: "Trưởng khoa",
        ssn: "0123456789",
        scheduler: {}
    })
      server.create("employee", {
        id: 16,
        lastName: "Nguyễn Văn",
        firstName: "P",
        type: "Y tá",
        faculty: "Thần kinh",
        status: "Khám bệnh",
        address: "268 Lý Thường Kiệt, Phường 14, Quận 10, TPHCM",
        dateBegin:  "2024-05-01",
        dateEnd: "2029-12-25",
        degree: [],
        dob: "2004-08-23",
        email: "nhu.nguyenquynh0109@hcmut.edu.vn",
        gender: "Nữ",
        jobTitle: "Tiến sĩ",
        med: "0123456789",
        phone: "0123456789",
        position: "Trưởng khoa",
        ssn: "0123456789",
        scheduler: {}
    })
      server.create("employee", {
        id: 17,
        lastName: "Nguyễn Văn",
        firstName: "Q",
        type: "Bác sĩ",
        faculty: "Tiêu hóa",
        status: "Trống",
        address: "268 Lý Thường Kiệt, Phường 14, Quận 10, TPHCM",
        dateBegin:  "2024-05-01",
        dateEnd: "2029-12-25",
        degree: [],
        dob: "2004-08-23",
        email: "nhu.nguyenquynh0109@hcmut.edu.vn",
        gender: "Nữ",
        jobTitle: "Tiến sĩ",
        med: "0123456789",
        phone: "0123456789",
        position: "Trưởng khoa",
        ssn: "0123456789",
        scheduler: {}
    })
      server.create("employee", {
        id: 18,
        lastName: "Nguyễn Văn",
        firstName: "R",
        type: "Bác sĩ",
        faculty: "Phụ sản",
        status: "Phẫu thuật",
        address: "268 Lý Thường Kiệt, Phường 14, Quận 10, TPHCM",
        dateBegin:  "2024-05-01",
        dateEnd: "2029-12-25",
        degree: [],
        dob: "2004-08-23",
        email: "nhu.nguyenquynh0109@hcmut.edu.vn",
        gender: "Nữ",
        jobTitle: "Tiến sĩ",
        med: "0123456789",
        phone: "0123456789",
        position: "Trưởng khoa",
        ssn: "0123456789",
        scheduler: {}
    })
      server.create("employee", {
        id: 19,
        lastName: "Nguyễn Văn",
        firstName: "S",
        type: "Khác",
        faculty: "Tiêu hóa",
        status: "Trống",
        address: "268 Lý Thường Kiệt, Phường 14, Quận 10, TPHCM",
        dateBegin:  "2024-05-01",
        dateEnd: "2029-12-25",
        degree: [],
        dob: "2004-08-23",
        email: "nhu.nguyenquynh0109@hcmut.edu.vn",
        gender: "Nữ",
        jobTitle: "Tiến sĩ",
        med: "0123456789",
        phone: "0123456789",
        position: "Trưởng khoa",
        ssn: "0123456789",
        scheduler: {}
    })
      server.create("employee", {
        id: 20,
        lastName: "Nguyễn Văn",
        firstName: "T",
        type: "Y tá",
        faculty: "Phụ sản",
        status: "Phẫu thuật",
        address: "268 Lý Thường Kiệt, Phường 14, Quận 10, TPHCM",
        dateBegin:  "2024-05-01",
        dateEnd: "2029-12-25",
        degree: [],
        dob: "2004-08-23",
        email: "nhu.nguyenquynh0109@hcmut.edu.vn",
        gender: "Nữ",
        jobTitle: "Tiến sĩ",
        med: "0123456789",
        phone: "0123456789",
        position: "Trưởng khoa",
        ssn: "0123456789",
        scheduler: {}
    })
    server.create("employee", {
      id: 21,
      address: "268 Lý Thường Kiệt, Phường 14, Quận 10, TPHCM",
      dateBegin:  "2024-05-01",
      dateEnd: "2029-12-25",
      degree: (2) ['Bằng bác sĩ', 'Chứng chỉ hành nghề'],
      dob: "2004-08-23",
      email: "nhu.nguyenquynh0109@hcmut.edu.vn",
      faculty: "Thần kinh",
      firstName: "Quỳnh Như",
      gender: "Nữ",
      imgURL: "blob:http://localhost:5173/09f7eb31-29dd-440d-8c84-b59d22f0817b",
      jobTitle: "Tiến sĩ",
      lastName: "Nguyễn",
      med: "0123456789",
      phone: "0123456789",
      position: "Trưởng khoa",
      ssn: "0123456789",
      type: "Bác sĩ",
      status: "Phẫu thuật",
      scheduler: {}
    })
    },

    routes() {
      // Define routes
      this.get("/api/employees", (schema) => {
        return schema.employees.all()
      })

      this.get("/api/employees/:id", (schema, request) => {
        let id = request.params.id
        return schema.employees.find(id)
      })

      this.post("/api/employees", (schema, request) => {
        let attrs = JSON.parse(request.requestBody)
        if (attrs.name) {
            return schema.employees.create(attrs) 
          } else {
            return new Response(
              400,
              { some: "header" },
              { errors: ["name cannot be blank"] }
            )
          }
      })

      this.delete("/api/employees/:id", (schema, request) => {
        let id = request.params.id
        return schema.employees.find(id).destroy()
      })

      this.patch("/api/employees/:id", function (schema, request) {
        let id = request.params.id
        let attrs = request.normalizedRequestAttrs() 
        return schema.employees.find(id).update(attrs) 
      })

      this.get("/api/employees/:id/event/list", (schema, request) => {
        let id = request.params.id
        return schema.employees.find(id).scheduler
      })

      this.post("/api/employees/:id/event/create", (schema, request) => {
        const id = request.params.id;
        const attrs = JSON.parse(request.requestBody);
      
        const employee = schema.employees.find(id);
      
        // Ensure the employee exists
        if (!employee) {
          return new Response(
            404,
            { "Content-Type": "application/json" },
            { errors: ["Employee not found"] }
          );
        }
      
        // Ensure the employee has a scheduler property
        if (!employee.scheduler) {
          employee.scheduler = {};
        }
      
        const { begin_date } = attrs;
      
        // Check if the begin_date already exists in the scheduler
        if (!employee.scheduler[begin_date]) {
          // If not, create a new array for the begin_date
          employee.scheduler[begin_date] = [];
        }
      
        // Add the new event to the scheduler
        employee.scheduler[begin_date].push(attrs);
      
        // Update the employee with the new scheduler
        employee.update({ scheduler: employee.scheduler });
      
        return new Response(
          200,
          { "Content-Type": "application/json" },
          { message: "Event created successfully", employee }
        );
      })
      
    
      
    },
  })
}
