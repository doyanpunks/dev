using Microsoft.AspNetCore.Mvc;

namespace kaspi_clone.Controllers
{
    public class HelloWorldController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
    }
}
