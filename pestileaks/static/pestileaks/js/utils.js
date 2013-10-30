function datatables_tastypie(source, oaData, callback, settings) {
    var $processing = $('.dataTables_processing', this.$el),
    	min_query_length = 3,
    	current_query = settings.oPreviousSearch.sSearch,
    	is_searching_number = !isNaN(parseFloat(current_query)),
	    sorting_column_names = [], i, sa, sorted_column_id, direction, ajax_data;

    for (i=0; i<settings.aaSorting.length; i++) {
        sa = settings.aaSorting[i];
        sorted_column_id = sa[0];
        direction = sa[1] === 'desc' ? '-' : '';
        sorted_column = settings.aoColumns[sorted_column_id];
        sorting_column_names.push(sorted_column.mData ? direction + sorted_column.mData : void 0);
    }
	ajax_data = {
      'limit': settings._iDisplayLength,
      'offset': settings._iDisplayStart
    };	
    if (sorting_column_names.length > 0) {
      ajax_data['order_by'] = sorting_column_names.join(',');
    }
    if (current_query !== '') {
      ajax_data['query'] = current_query;
    }
    if (current_query === '' || current_query.length >= min_query_length || is_searching_number) {
      $processing.show();
	  settings.jqXHR = $.ajax({
		url: source,
		data: ajax_data,
		success: function(data){
			console.log(data);
			data.echo = settings.iDraw;
			data.iTotalRecords = data.meta.total_count;
            data.iTotalDisplayRecords = data.meta.total_count;
			callback(data);
			}
		});
	} else {
		$processing.hide();
	}
}
var datatables_dutch = {
    "sProcessing": "Bezig...",
    "sLengthMenu": "_MENU_ resultaten weergeven",
    "sZeroRecords": "Geen resultaten gevonden",
    "sInfo": "_START_ tot _END_ van _TOTAL_ resultaten",
    "sInfoEmpty": "Geen resultaten om weer te geven",
    "sInfoFiltered": " (gefilterd uit _MAX_ resultaten)",
    "sInfoPostFix": "",
    "sSearch": "Zoeken:",
    "sEmptyTable": "Geen resultaten aanwezig in de tabel",
    "sInfoThousands": ".",
    "sLoadingRecords": "Een moment geduld aub - bezig met laden...",
    "oPaginate": {
        "sFirst": "Eerste",
        "sLast": "Laatste",
        "sNext": "Volgende",
        "sPrevious": "Vorige"
    }
};
