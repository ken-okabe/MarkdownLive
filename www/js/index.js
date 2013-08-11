(function() //-----
	{
		"use strict";

		$(document)
			.ready(function()
			{ //--------------------------
				$('#streamDIV')
					.html('<h1>MarkdownLive</h1><h3>Markdown Streaming Live View for SublimeText3</h3><br><h4><strong>Open</strong> <br><br>.md<br>.markdown<br>.mdown<br>.mkdn<br>.mkd<br>.mdwn<br>.mdtxt<br>.mdtext<br>.text<br>.txt</h4>');
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