using Microsoft.AspNetCore.Mvc;
using ToDoList.Server.Models;
using ToDoList.Server.Repositories;

namespace ToDoList.Server.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class TodoController : ControllerBase
    {
        private readonly ITodoRepository _repository;

        public TodoController(ITodoRepository repository)
        {
            _repository = repository;
        }

        [HttpGet]
        public async Task<ActionResult<IEnumerable<TodoItem>>> GetAll()
        {
            var items = await _repository.GetAllAsync();
            return Ok(items);
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<TodoItem>> GetById(int id)
        {
            var item = await _repository.GetByIdAsync(id);
            if (item == null)
                return NotFound();

            return Ok(item);
        }

        [HttpPost]
        public async Task<ActionResult<TodoItem>> Create(TodoItem item)
        {
            var created = await _repository.CreateAsync(item);
            return CreatedAtAction(nameof(GetById), new { id = created.Id }, created);
        }

        [HttpPut("{id}")]
        public async Task<IActionResult> Update(int id, TodoItem item)
        {
            if (id != item.Id)
                return BadRequest();

            await _repository.UpdateAsync(item);
            return NoContent();
        }

        [HttpDelete("{id}")]
        public async Task<IActionResult> Delete(int id)
        {
            await _repository.DeleteAsync(id);
            return NoContent();
        }
    }
}
