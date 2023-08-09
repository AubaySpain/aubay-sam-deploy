from string import Template


class HTMLBlocks:

    page = Template('''
      <html>
        <head>
          <title>
            Activo
          </title>
          <link href="http://ostranme.github.io/swagger-ui-themes/demo/images/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
          <link href="http://ostranme.github.io/swagger-ui-themes/demo/css/typography.css" rel="stylesheet" type="text/css"/>
          <link href="http://ostranme.github.io/swagger-ui-themes/demo/css/reset.css" rel="stylesheet" type="text/css"/>
          <link href="http://ostranme.github.io/swagger-ui-themes/demo/css/screen.css" rel="stylesheet" type="text/css"/>
          <style>
            .swagger-section .swagger-ui-wrap ul#resources li.resource ul.endpoints li.endpoint ul.operations li.operation.none div.content {
              background-color: #ddd8d2;
              border: 1px solid #f0e0ca;
            }
            .swagger-section .swagger-ui-wrap ul#resources li.resource ul.endpoints li.endpoint ul.operations li.operation.good div.content {
              background-color: #f6f9e3;
              border: 1px solid #f2f77f;
            }
            .swagger-section .swagger-ui-wrap ul#resources li.resource ul.endpoints li.endpoint ul.operations li.operation div.heading h3 span.http_method a {
              text-transform: uppercase;
              color: white;
              display: inline-block;
              width: 70px;
              font-size: 0.7em;
              text-align: center;
              padding: 7px 10 4px;
              -moz-border-radius: 2px;
              -webkit-border-radius: 2px;
              -o-border-radius: 2px;
              -ms-border-radius: 2px;
              -khtml-border-radius: 2px;
              border-radius: 2px;
            }
            .swagger-section .swagger-ui-wrap {
              min-width: 760px;
              max-width: 1400px;
            }
            .swagger-section .swagger-ui-wrap ul#resources li.resource ul.endpoints li.endpoint ul.operations.grupal {
              padding-bottom: 12px;
            }
            .swagger-section .swagger-ui-wrap ul#resources li.resource ul.endpoints li.endpoint ul.operations.grupal>li div.heading {
              background-color: burlywood;
            }
            .swagger-section .swagger-ui-wrap ul#resources li.resource ul.endpoints li.endpoint ul.operations.grupal>li div.heading h2 {
              color: white;
              padding-left: 12px;
            }
          </style>
        </head>
        <body class="swagger-section">
          <div id="header">
            <div class="swagger-ui-wrap">
              <a id="logo" href="http://swagger.io/">
                <img class="logo__img" alt="IsyHub-Aubay-Logo" height="30"
                  src="https://lab.isyhub.net/assets/theme/isyhub/images/logos/default.png">
                <span class="logo__title">
                  Activos
                </span>
              </a>
            </div>
          </div>
          <div id="swagger-ui-container" class="swagger-ui-wrap">
            <ul id="resources">
              ${content}
            </ul>
          </div>
        </body>
      </html>
    ''')

    info = Template('''
      <li class="resource active">
        <div class="heading">
          <h2>
            Información General
          </h2>
          <ul class="endpoints">
            <li class="endpoint">
              <ul class="operations">
                <li class="post operation">
                  <div class="heading">
                    <h3>
                      <span class="http_method">
                        <a href="" class="toggleOperation">
                          Nombre
                        </a>
                      </span>
                      <span class="path">
                        <a href="" class="toggleOperation">
                          ${name}
                        </a>
                      </span>
                    </h3>
                  </div>
                  <div class="content">
                    <div class="response-class">
                      <h4>
                        <span>
                          Descripción
                        </span>
                      </h4>
                      <div class="markdown">
                        <p>
                          ${description}
                        </p>
                      </div>
                      <br>
                    </div>
                    <form accept-charset="UTF-8" class="sandbox">
                      <table class="fullwidth parameters">
                        <tbody class="operation-params">
                          ${items}
                        </tbody>
                      </table>
                    </form>
                  </div>
                </li>
              </ul>
            </li>
          </ul>
        </div>
      </li>
    ''')

    items = Template('''
      <tr>
        <td class="code required">
          <label>
            ${key}
          </label>
        </td>
        <td>
          <strong>
            <span class="markdown">
              <p>
                ${value}
              </p>
            </span>
          </strong>
        </td>
        <td>
          ${title}
        </td>
      </tr>
    ''')

    props = Template('''
      <li class="resource">
        <div class="heading">
          <h2>
            ${title}
          </h2>
          <ul class="endpoints">
            <li class="endpoint">
              <ul class="${classes}">
                ${items}
              </ul>
            </li>
          </ul>
        </div>
      </li>
    ''')

    props_item = Template('''
      <li class="${classes}">
        <div class="content">
          <form accept-charset="UTF-8" class="sandbox">
            <table class="fullwidth parameters">
              <thead>
                <tr>
                  ${labels}
                </tr>
              </thead>
              <tbody class="operation-params">
                ${items}
              </tbody>
            </table>
          </form>
        </div>
      </li>
    ''')

    props_label = Template('''
      <th style="width: 100px; max-width: 100px">
        ${label}
      </th>
    ''')

    props_value = Template('''
      <td class="code">
        <label>
          ${value}
        </label>
      </td>
    ''')
