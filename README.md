This project is a full-stack To-Do List application with a .NET 9 server and a modern React/TypeScript front end. It provides robust CRUD operations for managing tasks, designed for maintainability, scalability, and efficient development workflows.

***

# ToDoList Application

## Overview

A robust, extensible To-Do List application built with ASP.NET Core (server) and React (client). Designed with clear separation of concerns and clean architecture, it provides persistent task management backed by SQL Server and a rich client experience using the latest React and TypeScript standards.

***

## Features

- Create, read, update, and delete (CRUD) to-do items.
- Mark tasks as completed, with timestamps.
- Items have title, description, created/completed dates, and status.
- RESTful API built with ASP.NET Core, leveraging Entity Framework Core for data access.
- Modern frontend with React, TypeScript, and Vite for rapid development.

***

## Tech Stack

| Layer            | Stack & Tools                |
|------------------|-----------------------------|
| Backend (API)    | ASP.NET Core 9, EF Core 9, SQL Server |
| Frontend (SPA)   | React 19, TypeScript 5.8, Vite 7 |
| Communication    | REST API with JSON payloads |
| Tooling & DevOps | ESLint, TypeScript ESLint, Hot Reload |

***

## Getting Started

### Prerequisites

- .NET 9 SDK
- Node.js (>=18)
- SQL Server (localdb or equivalent)

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

- `ToDoList.Server/`: .NET Core Web API with EF Core models, repositories, controllers.
- `todolist.client/`: React SPA with TypeScript, Vite, ESLint configs, and modular components.

***

## Development and Linting

- **Backend:** C# best practices, automated migrations with EF Core.
- **Frontend:** Hot reloading, strict linting (ESLint + React Hooks), type safety (TypeScript).

***

## License

This project is provided under the MIT License.

***

## Contributing

Open source contributions are welcome. Please submit pull requests following project coding styles and best practices.

***

For questions or feature discussions, please open an issue!
