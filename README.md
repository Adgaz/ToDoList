This project is a full-stack To-Do List application with a .NET 9 server and a modern React/TypeScript front end. It provides robust CRUD operations for managing tasks, designed for maintainability, scalability, and efficient development workflows.[1][2]

***

# ToDoList Application

## Overview

A robust, extensible To-Do List application built with ASP.NET Core (server) and React (client). Designed with clear separation of concerns and clean architecture, it provides persistent task management backed by SQL Server and a rich client experience using the latest React and TypeScript standards.[2][1]

***

## Features

- Create, read, update, and delete (CRUD) to-do items.[1]
- Mark tasks as completed, with timestamps.[1]
- Items have title, description, created/completed dates, and status.[1]
- RESTful API built with ASP.NET Core, leveraging Entity Framework Core for data access.[1]
- Modern frontend with React, TypeScript, and Vite for rapid development.[2]

***

## Tech Stack

| Layer            | Stack & Tools                |
|------------------|-----------------------------|
| Backend (API)    | ASP.NET Core 9, EF Core 9, SQL Server[1] |
| Frontend (SPA)   | React 19, TypeScript 5.8, Vite 7[2] |
| Communication    | REST API with JSON payloads[1] |
| Tooling & DevOps | ESLint, TypeScript ESLint, Hot Reload[2] |

***

## Getting Started

### Prerequisites

- .NET 9 SDK[1]
- Node.js (>=18)[2]
- SQL Server (localdb or equivalent)[1]

### Backend Setup

1. Navigate to the `ToDoList.Server` project directory.
2. Restore dependencies:  
   `dotnet restore`
3. Update the DB (localdb default):  
   `dotnet ef database update`
4. Start the server:  
   `dotnet run`

### Frontend Setup

1. Navigate to the `todolist.client` project directory.
2. Restore npm dependencies:  
   `npm install`
3. Launch the development server:  
   `npm run dev`
4. Access the SPA at `http://localhost:54420`

### API Endpoints

| Method | Path                  | Description                     |
|--------|-----------------------|---------------------------------|
| GET    | `/api/todo`           | Get all to-do items             |
| GET    | `/api/todo/{id}`      | Get item by ID                  |
| POST   | `/api/todo`           | Create a new item               |
| PUT    | `/api/todo/{id}`      | Update an item                  |
| DELETE | `/api/todo/{id}`      | Delete an item                  |


***

## Project Structure

- `ToDoList.Server/`: .NET Core Web API with EF Core models, repositories, controllers.[1]
- `todolist.client/`: React SPA with TypeScript, Vite, ESLint configs, and modular components.[2]

***

## Development and Linting

- **Backend:** C# best practices, automated migrations with EF Core.[1]
- **Frontend:** Hot reloading, strict linting (ESLint + React Hooks), type safety (TypeScript).[2]

***

## License

This project is provided under the MIT License.[2]

***

## Contributing

Open source contributions are welcome. Please submit pull requests following project coding styles and best practices.

***

For questions or feature discussions, please open an issue!

[1](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/95785945/c0c6ffdd-81f6-445e-8ed1-3eaff83d1c5a/ToDoList.Server.txt)
[2](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/95785945/5510d4a8-c634-48d8-9dc0-df67daefe7be/todolist.client.txt)
