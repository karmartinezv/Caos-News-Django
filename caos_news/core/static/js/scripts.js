$(document).ready(
    cargarApi
);

function cargarApi() {
    $.getJSON('https://mindicador.cl/api', function (data) {
        var dailyIndicators = data;
        var indicadores = "Indicadores Diarios: Bitcoin " + formatoMoneda(dailyIndicators.bitcoin.valor * dailyIndicators.dolar.valor) + " --- ";
        indicadores = indicadores + " USD " + formatoMoneda(dailyIndicators.dolar.valor) + " --- ";
        indicadores = indicadores + " EURO " + formatoMoneda(dailyIndicators.euro.valor) + " --- ";
        indicadores = indicadores + " IMACEC " + dailyIndicators.imacec.valor + "%" + " --- ";
        indicadores = indicadores + " IPC " + dailyIndicators.ipc.valor + "%" + " --- ";
        indicadores = indicadores + " IVP " + formatoMoneda(dailyIndicators.ivp.valor);
        indicadores = indicadores + " LIBRA COBRE " + formatoMoneda(dailyIndicators.libra_cobre.valor * dailyIndicators.dolar.valor) + " --- ";
        indicadores = indicadores + " TASA DESEMPLEO " + dailyIndicators.tasa_desempleo.valor + "%" + " --- ";
        indicadores = indicadores + " TPM " + dailyIndicators.tpm.valor + "%" + " --- ";
        indicadores = indicadores + " UF " + formatoMoneda(dailyIndicators.uf.valor) + " --- ";
        indicadores = indicadores + " UTM " + formatoMoneda(dailyIndicators.utm.valor);
        $("#indicadoresDiarios").html(indicadores);
    }).fail(function () {
        console.log('Error al consumir la API!');
    })
    $.getJSON('https://api.gael.cloud/general/public/clima', function (data) {
        var clima = new Array();
        clima = data;
        var tbody = $("#tblClima");
        for (var i = 0; i < clima.length; i++) {
            var { Estacion, Estado, HoraUpdate, Humedad, Temp } = clima[i];
            var elemento = "<tr>"
            elemento = elemento + "<td class='text-center'>" + Estacion + "</td>";
            elemento = elemento + "<td class='text-center'>" + Humedad + "%</td>";
            elemento = elemento + "<td class='text-center'>" + Temp + "°C</td>";
            tbody.append(elemento);
            $("#horaUpdate").html(HoraUpdate);
        }
    }).fail(function () {
        console.log('Error al consumir la API!');
    })
}

function formatoMoneda(valor) {
    const formato = new Intl.NumberFormat(
        'es-CL',
        {
            style: 'currency',
            currency: 'CLP',
            minimumFractionDigits: 2
        }
    )

    return formato.format(valor);
}

function login() {
    $.ajax({
        type: "POST",
        url: "login",
        data: {
            user: $("#txtUser").val(),
            pass: $("#txtPass").val()
        },
        success: function (resultado) {
            console.log(resultado);
        }
    });
    return false;
}

function procesarForm() {
    estado = false;

    var idCategoria = $("#cmbCategorias").val();

    if (idCategoria === null) {
        swal({
            title: "Error",
            text: "Seleccionar Categoría",
            icon: "error",
            button: true
        });
    } else {
        estado = true;
    }

    return estado;
}

