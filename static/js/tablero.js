function copiar() {
    var copiarTexto = document.getElementById("MiEntrada");

    copiarTexto.select();
    copiar.setSelectionRange(0, 100);

    navigator.clipboard.writeText(copiarTexto.value);

    alert("Copiar codigo:" +copiarTexto.value);
    
}