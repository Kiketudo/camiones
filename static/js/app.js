function allowDrop(event) {
    event.preventDefault();
    const column = event.currentTarget;
    column.style.border = '2px dashed blue';
}

function drag(event) {
    event.dataTransfer.setData("text/plain", event.target.id);
}

function dragLeave(event) {
    event.target.closest('.kanban-column').style.border = '1px solid #ccc';
}

function drop(event) {
    event.preventDefault();
    const column = event.currentTarget;
    column.style.border = '1px solid #ccc';
    const id = event.dataTransfer.getData("text/plain");
    const item = document.getElementById(id);
    if (item) {
        const currentColumn = item.parentNode;
        if (currentColumn !== column.querySelector('.kanban-items')) {
            column.querySelector('.kanban-items').appendChild(item);
        }
    } else {
        console.error(`Elemento con ID ${id} no encontrado.`);
    }
    
}
function abrirModal(matricula) {
    document.getElementById('modal-' + matricula).style.display = 'block';
}

function cerrarModal(matricula) {
    document.getElementById('modal-' + matricula).style.display = 'none';
}
function comprobarEstado() {
    fetch('/comprobar_estado')
        .catch(error => console.error('Error en la solicitud:', error));
}
function searchTruck() {
    // Obtener el valor de búsqueda
    const searchTerm = document.getElementById("search-matricula").value.toLowerCase();
    const trucks = document.querySelectorAll(".kanban-item");
    const trucks1 = document.querySelectorAll(".kanban-item1");
    // Recorrer cada elemento y mostrarlo u ocultarlo según la coincidencia en 'data-agencia'
    trucks.forEach(truck => {
        const agencyElement = truck.querySelector(".matricula");
        const agencyText = agencyElement ? agencyElement.textContent.toLowerCase() : "";
        truck.style.display = agencyText.includes(searchTerm) ? "grid" : "none";
    });
    trucks1.forEach(function(truck1) {
        const agencyElement = truck1.querySelector(".matricula");
        const agencyText = agencyElement ? agencyElement.textContent.toLowerCase() : "";
        
        if (agencyText.includes(searchTerm)) {
            truck1.style.display = "grid"; // Mostrar camión si la matrícula coincide
        } else {
            truck1.style.display = "none"; // Ocultar camión si la matrícula no coincide
        }
    });
}

function searchAgency() {
    // Obtener el valor del campo de búsqueda
    const searchTerm = document.getElementById("search-agencia").value.toLowerCase();

    // Seleccionar todos los elementos con clase 'kanban-item'
    const trucks = document.querySelectorAll(".kanban-item");
    const trucks1 = document.querySelectorAll(".kanban-item1");
    // Recorrer cada elemento y mostrarlo u ocultarlo según la coincidencia en 'data-agencia'
    trucks.forEach(truck => {
        const agencyElement = truck.querySelector(".agencia");
        const agencyText = agencyElement ? agencyElement.textContent.toLowerCase() : "";
        truck.style.display = agencyText.includes(searchTerm) ? "grid" : "none";
    });
    trucks1.forEach(function(truck1) {
        const agencyElement = truck1.querySelector(".agencia");
        const agencyText = agencyElement ? agencyElement.textContent.toLowerCase() : "";
        
        if (agencyText.includes(searchTerm)) {
            truck1.style.display = "grid"; // Mostrar camión si la matrícula coincide
        } else {
            truck1.style.display = "none"; // Ocultar camión si la matrícula no coincide
        }
    });
}
function marcarPreparado(Id) {
    fetch('/preparar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ Id: Id }),
    })
    .then(response => {
        if (response.ok) {
            alert('El camión ha sido marcado como preparado.');
            location.reload();
        } else {
            alert('Error al marcar como preparado.');
        }
    })
    .catch(error => console.error('Error:', error));
}
function confirmarReset() {
    if (confirm("¿Estás seguro de que deseas resetear la tabla? Esta acción no se puede deshacer.")) {
        window.location.href = "/resetear-tabla"; // Redirige a la ruta Flask
    }
}
document.getElementById('mas').addEventListener('click', function() {
    window.location.href ='/add';
});
// Llama a comprobarEstado cada minuto
setInterval(comprobarEstado, 60000);