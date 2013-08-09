(function() //-----
	{
		"use strict";

		$(document)
			.ready(function()
			{ //--------------------------
				$('#streamDIV')
					.html('<h2>MarkdownLive Ready. <h3>Open <br>.md<br>.markdown<br>.mdown<br>.mkdn<br>.mkd<br>.mdwn<br>.mdtxt<br>.mdtext<br>.text<br>.txt</h3>');
				var through = require('through');

				var stream = require('shoe')('/stream')
					.pipe(through(function(data)
					{
						$('#streamDIV')
							.html(data);
					}));
				//-------------------------
			});

	}());