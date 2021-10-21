function copiar() {
    var copiarTexto = document.getElementById("MiEntrada");

    copiarTexto.select();
    copiarTexto.setSelectionRange(0, 5);

    navigator.clipboard.writeText(copiarTexto.value);

    alert("Ha copiado el siguiente codigo = !" + copiarTexto.value);
    
}