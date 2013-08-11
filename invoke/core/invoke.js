(function()
{
    'use strict';

    $('document')
        .ready(function()
        {
            $("body")
                .load("/invoke/scheme.html", function()
                {
                    console.log('scheme loaded');

                    marked.setOptions(
                    {
                        gfm: true,
                        tables: true,
                        breaks: true,
                        pedantic: true,
                        sanitize: false,
                        smartLists: false,
                        smartypants: true,
                        langPrefix: 'lang-',
                        highlight: function(code)
                        {
                            return hljs.highlightAuto(code)
                                .value;
                        }
                    });

                    var newlinesAsIs = true;

                    $.get('./entry.md', function(data)
                    {
                        var data2;
                        if (newlinesAsIs)
                        {
                            data2 = '<style type="text/css">p {margin: 0}</style>' +
                                marked(hack(data));
                        }
                        else
                        {
                            data2 = marked(data);
                        }

                        $('#streamDIV')
                            .html(data2);
                        $("body")
                            .show();
                    });


                });
        });

    String.prototype.replaceAll = function(org, dest)
    {
        return this.split(org)
            .join(dest);
    };

    var hack = function(data0)
    {
        //list hack 
        var data7 = data0.replace(/(- [\s\S]+?)(?:\n\n)/g, '$1\n&nbsp;\n');
        var data8 = data7.replace(/(- [\s\S]+?)(?:\n&nbsp;\n\n)/g, '$1\n\n\n\n\n');
        var data9 = data8.replace(/\n&nbsp;\n(?=[^-])/g, '\n\n\n'); //ok
        var data = data9; //.replace(/\n\n(?=- )/g, '\n\n');

        var rxCodeG = /<code>[\s\S]+?<\/code>|<pre>[\s\S]+?<\/pre>|\n```+[\s\S]+?```+|\n- [\s\S]+?\n\n/g;
        var rxCode = /<code>[\s\S]+?<\/code>|<pre>[\s\S]+?<\/pre>|\n```+[\s\S]+?```+|\n- [\s\S]+?\n\n/;

        var codes = data.match(rxCodeG);
        var codeKey = 'thisistheCodeKey';
        var data1 = [];
        var data1L;
        if (codes)
        {
            codes.map(
                function() //ideally use return
                {
                    var len = data1.length;
                    var src;
                    if (len === 0)
                    {
                        src = data;
                    }
                    else
                    {
                        src = data1[len - 1];
                    }
                    data1[len] = src.replace(rxCode, codeKey + len);
                });
            data1L = data1[data1.length - 1];
        }
        else
        {
            data1L = data;
        }

        var escape1 = 'thisisdummy3141592escape1';
        var escape2 = 'thisisdummy3141592escape2';
        var toReplace = '&nbsp;' + '\n\n';

        var data2 = data1L
            .replace(/(^|[^\n])\n(?!\n)/g, '$1' + escape1)
            .replace(/(^|[^\n])\n{2}/g, '$1' + escape2)
            .replace(/\n/g, toReplace)
            .replaceAll(escape1, '\n')
            .replaceAll(escape2, '\n\n' + toReplace);

        var data3 = [];
        var data3L;
        if (codes)
        {
            codes.map(
                function()
                {
                    var len = data3.length;
                    var src;
                    if (len === 0)
                    {
                        src = data2;
                    }
                    else
                    {
                        src = data3[len - 1];
                    }
                    data3[len] = src.replace(codeKey + len, codes[len]);
                });
            data3L = data3[data3.length - 1];
        }
        else
        {
            data3L = data2;
        }

        return data3L;
    };

}());