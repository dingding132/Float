$(window).ready(function(){
	      var nowTemp = new Date();
	      var now = new Date(nowTemp.getFullYear(), nowTemp.getMonth(), nowTemp.getDate(), 0, 0, 0, 0);
	     	/* checkin = $('#checkin').datepicker({
	        onRender: function(date) {
	          return date.valueOf() < now.valueOf() ? 'disabled' : '';
	        }
	      }).on('changeDate', function(ev) {
	        if (ev.date.valueOf() > checkout.date.valueOf()) {
	          var newDate = new Date(ev.date)
	          newDate.setDate(newDate.getDate() + 1);
	          checkout.setValue(newDate);
	        }
	        checkin.hide();
	        $('#checkout')[0].focus();
	      }).data('datepickr');*/
	      var chekcout = $('#date').datepicker({
	        onRender: function(date) {
	          return date.valueOf() <= checkin.date.valueOf() ? 'disabled' : '';
	        }
	      }).on('changeDate', function(ev) {
	        checkout.hide();
	      }).data('datepicker');
});
