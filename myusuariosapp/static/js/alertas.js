function confirmaEliminar(purl){
    console.log(purl);
    $.confirm({
        title: 'Confirmación',
        content: '¿Desea eliminar el registro?',
        type: 'orange',
        icon: 'glyphicon glyphicon-warning-sign',
        buttons: {
            Eliminar: function () {
                console.log(purl);
                document.location.href = purl;
            },
            Cancelar: function () {
                document.location.href = '#';
            }
        }
    });
}
