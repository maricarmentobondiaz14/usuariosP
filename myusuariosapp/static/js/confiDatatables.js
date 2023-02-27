$(document).ready(function () {
    $('#tablausuarios1').DataTable({
       columnDefs: [
            //Definir ancho estático para las primeras dos columnas
            {width    : "20px", targets: [0, 1]},
            //Eliminar flechas de ordenamiento para las primeras dos columnas
            {sortable : false, targets: [0, 1]},
        ],
    bFilter: false,


        language: {
            search: "Buscar:",
            lengthMenu: "No. de Resultados _MENU_ ",
            info: "Mostrando del usuario _START_ al _END_ de un total de _TOTAL_ usuarios",
            infoEmpty: "No existen datos.",
            loadingRecords: "Cargando...",
            zeroRecords: "No se encontraron datos con tu búsqueda",
            emptyTable: "No hay datos Disponibles en la tabla",
            infoFiltered: "(filtrado de _MAX_ elementos en total)",
            paginate: {
                first: "Primero",
                previous: "Anterior",
                next: "Siguiente",
                last: "Último"
            }
        },

        //Definir alto estático del Datatable
        scrollY:  300,
        scrollX: "100%",
        scrollXInner: "150%",

        //Definir Opciones del Número de Resultados a mostrar
        lengthMenu: [ [10, 15, -1], [10, 15, "Todos"] ],



    });
});