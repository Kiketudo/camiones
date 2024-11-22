function addTruckEntry(truckData) {
    const truckContainer = document.getElementById('truck-container');
    
    // Crear un nuevo conjunto de campos para un camión
    const newTruckEntry = document.createElement('div');
    newTruckEntry.classList.add('truck-entry');

    newTruckEntry.innerHTML = `
        <button type="button" class="remove-truck-btn">&times;</button> 
        <label for="truck-number">Truck Number:</label>
        <input type="text" name="truck_number[]" value="${truckData[0]}">

        <label for="truck-age">Agencia:</label>
        <input type="text" name="agencia[]" value="${truckData[1]}">

        <label for="truck-destiny">Destino:</label>
        <input type="text" name="destino[]" value="${truckData[2]}">

        <label for="truck-obs">Observación:</label>
        <input type="text" name="observacion[]" value="${truckData[3]}">
    `;
    console.log(newTruckEntry);
    const removeButton = newTruckEntry.querySelector('.remove-truck-btn');
    removeButton.addEventListener('click', function () {
        truckContainer.removeChild(newTruckEntry);
    });
    
    truckContainer.appendChild(newTruckEntry);
}

document.querySelectorAll('.remove-truck-btn').forEach(button => {
    button.addEventListener('click', function () {
        const truckEntry = button.parentElement; // Obtener el contenedor padre
        truckEntry.remove(); // Eliminar el contenedor
    });
});

document.getElementById('paste-data').addEventListener('paste', function(event) {
    // Obtener los datos pegados (como texto plano)
    const pastedData = event.clipboardData.getData('text');

    // Limpiar el texto pegado (por si hay saltos de línea o espacios adicionales)
    const cleanData = pastedData.trim();

    // Dividir los datos en líneas (cada línea será un camión)
    const truckLines = cleanData.split('\n'); // Divide por líneas

    truckLines.forEach(function(line) {
        // Dividir cada línea en campos (pueden estar separados por tabulaciones o espacios)
        const truckData = line.trim().split(/\s+/); // Divide por uno o más espacios/tabulaciones

        // Verificamos si la línea tiene entre 3 y 4 campos (como máximo 4 campos)
        
            // Añadir un nuevo conjunto de campos al formulario
            addTruckEntry(truckData);
        })
});

// Función para añadir un nuevo formulario de camión (opcional si el usuario desea añadir manualmente)
document.getElementById('add-truck-btn').addEventListener('click', function() {
    const truckContainer = document.getElementById('truck-container');
    
    // Crear un nuevo conjunto de campos para un camión
    const newTruckEntry = document.createElement('div');
    newTruckEntry.classList.add('truck-entry');

    newTruckEntry.innerHTML = `
        <button type="button" class="remove-truck-btn">&times;</button> 
        <label for="truck-number">Truck Number:</label>
        <input type="text" name="truck_number[]">

        <label for="truck-age">Agencia:</label>
        <input type="text" name="agencia[]">

        <label for="truck-destiny">Destino:</label>
        <input type="text" name="destino[]">

        <label for="truck-obs">Observación:</label>
        <input type="text" name="observacion[]">

    `;
    console.log(newTruckEntry);
    const removeButton = newTruckEntry.querySelector('.remove-truck-btn');
    removeButton.addEventListener('click', function () {
        truckContainer.removeChild(newTruckEntry);
    });
    
    truckContainer.appendChild(newTruckEntry);
});