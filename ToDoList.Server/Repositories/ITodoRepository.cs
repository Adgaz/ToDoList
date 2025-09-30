using ToDoList.Server.Models;

namespace ToDoList.Server.Repositories
{
    public interface ITodoRepository
    {
        Task<IEnumerable<TodoItem>> GetAllAsync();
        Task<TodoItem?> GetByIdAsync(int id);
        Task<TodoItem> CreateAsync(TodoItem item);
        Task UpdateAsync(TodoItem item);
        Task DeleteAsync(int id);
    }
}