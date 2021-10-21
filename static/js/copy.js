function copiar() {
    var copiarTexto = document.getElementById("MiEntrada");

    copiarTexto.select();
    copiarTexto.setSelectionRange(0, 5);

    navigator.clipboard.writeText(copiarTexto.value);

    alert("Su codigo ha sido copiado = " + copiarTexto.value);
    
}

