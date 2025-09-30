import { useState, useEffect } from 'react';
import { todoService } from './services/todoService';
import type { TodoItem } from './types/Todo';  // Add 'type' keyword
import './App.css';

function App() {
    const [todos, setTodos] = useState<TodoItem[]>([]);
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    // Load todos when component mounts
    useEffect(() => {
        loadTodos();
    }, []);

    const loadTodos = async () => {
        try {
            setLoading(true);
            const data = await todoService.getAll();
            setTodos(data);
            setError(null);
        } catch (err) {
            setError('Failed to load todos');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();

        if (!title.trim()) return;

        try {
            const newTodo = {
                title: title.trim(),
                description: description.trim() || null,
                isCompleted: false,
                createdAt: new Date(),
                completedAt: null
            };

            await todoService.create(newTodo);
            setTitle('');
            setDescription('');
            await loadTodos(); // Reload the list
        } catch (err) {
            setError('Failed to create todo');
            console.error(err);
        }
    };

    const toggleComplete = async (todo: TodoItem) => {
        try {
            const updated = {
                ...todo,
                isCompleted: !todo.isCompleted,
                completedAt: !todo.isCompleted ? new Date() : null
            };

            await todoService.update(todo.id, updated);
            await loadTodos();
        } catch (err) {
            setError('Failed to update todo');
            console.error(err);
        }
    };

    const deleteTodo = async (id: number) => {
        try {
            await todoService.delete(id);
            await loadTodos();
        } catch (err) {
            setError('Failed to delete todo');
            console.error(err);
        }
    };

    return (
        <div className="app">
            <div className="todo-container">
                <h1>My Todo List</h1>

                {error && <div className="error">{error}</div>}

                {/* Add Todo Form */}
                <form onSubmit={handleSubmit} className="todo-form">
                    <input
                        type="text"
                        placeholder="Task title..."
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                        className="input-title"
                    />
                    <input
                        type="text"
                        placeholder="Description (optional)..."
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                        className="input-description"
                    />
                    <button type="submit" className="btn-add">
                        Add Task
                    </button>
                </form>

                {/* Todo List */}
                {loading ? (
                    <div className="loading">Loading...</div>
                ) : (
                    <ul className="todo-list">
                        {todos.length === 0 ? (
                            <li className="empty-state">No todos yet. Add one above!</li>
                        ) : (
                            todos.map((todo) => (
                                <li
                                    key={todo.id}
                                    className={`todo-item ${todo.isCompleted ? 'completed' : ''}`}
                                >
                                    <div className="todo-content">
                                        <input
                                            type="checkbox"
                                            checked={todo.isCompleted}
                                            onChange={() => toggleComplete(todo)}
                                            className="checkbox"
                                        />
                                        <div className="todo-text">
                                            <h3>{todo.title}</h3>
                                            {todo.description && <p>{todo.description}</p>}
                                        </div>
                                    </div>
                                    <button
                                        onClick={() => deleteTodo(todo.id)}
                                        className="btn-delete"
                                    >
                                        Delete
                                    </button>
                                </li>
                            ))
                        )}
                    </ul>
                )}
            </div>
        </div>
    );
}

export default App;
