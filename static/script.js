// function toggleDepartamentos(header) {
//     let departamentos = header.nextElementSibling;
//     departamentos.classList.toggle('hidden');
// }

// function toggleFuncionarios(header) {
//     let funcionarios = header.nextElementSibling;
//     funcionarios.classList.toggle('hidden');
// }

function toggleDepartamentos(header) {
    let departamentos = header.nextElementSibling;
    departamentos.classList.toggle('hidden');
    
    let button = header.querySelector('button');
    let expanded = !departamentos.classList.contains('hidden');
    button.innerText = expanded ? '-' : '+';
}

function toggleFuncionarios(header) {
    let funcionarios = header.nextElementSibling;
    funcionarios.classList.toggle('hidden');
    
    let button = header.querySelector('button');
    let expanded = !funcionarios.classList.contains('hidden');
    button.innerText = expanded ? '-' : '+';
}
