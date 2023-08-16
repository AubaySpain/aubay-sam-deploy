
class HTML:

    @staticmethod
    def page(content):
        return f'''
          <html>
            <head>
              <title>
                Activo
              </title>
              <link href="http://ostranme.github.io/swagger-ui-themes/demo/images/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
              <link href="http://ostranme.github.io/swagger-ui-themes/demo/css/reset.css" rel="stylesheet" type="text/css"/>
              <link href="http://ostranme.github.io/swagger-ui-themes/demo/css/screen.css" rel="stylesheet" type="text/css"/>
              <link href="http://ostranme.github.io/swagger-ui-themes/demo/css/typography.css" rel="stylesheet" type="text/css"/>
              <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400&display=swap" rel="stylesheet">
              <style>
                #name {{
                  text-transform: uppercase;
                  text-decoration: none;
                  color: white;
                  background-color: #10a54a;
                  display: inline-block;
                  width: 70px;
                  font-size: 0.7em;
                  text-align: center;
                  padding: 7px 10 4px;
                  border-radius: 2px;
                }}
                #description {{
                  color: #10a54a;
                }}
                .swagger-section .swagger-ui-wrap {{
                  min-width: 760px;
                  max-width: 1400px;
                }}
                .operation {{
                  border-radius: 4px;
                  font-family: 'Open Sans', sans-serif;
                  font-weight: 400;
                }}
                .grupal {{
                  padding-bottom: 20px;
                }}
                .grupal div.heading {{
                  background-color: burlywood;
                }}
                .grupal div.heading h2 {{
                  color: white !important;
                  padding-left: 12px !important;
                }}
                .mint div.heading {{
                  background-color: #ebf7f0;
                  border: 1px solid #c3e8d1 !important;
                }}
                .mint div.content {{
                  background-color: #ebf7f0;
                  border: 1px solid #c3e8d1;
                }}
                .blue div.content {{
                  background-color: #ebf3f9;
                  border: 1px solid #c3d9ec !important;
                }}
                .green div.content {{
                  background-color: #eff9e3;
                  border: 1px solid #cfddb8 !important;
                }}
                .brown div.content {{
                  background-color: #faf5ee;
                  border: 1px solid #f0e0ca !important;
                }}
                .bold td {{
                  font-weight: bold !important;
                }}
                .path a {{
                  text-decoration: none !important;
                }}
                .subtable td {{
                  border: none !important;
                }}
                li {{
                  margin-bottom: 8px;
                }}
                li:last-child {{
                  margin-bottom: 0;
                }}
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
              <div class="swagger-ui-wrap">
                <ul id="resources">
                  {content}
                </ul>
              </div>
              <script>
                function collapseSection(id) {{
                  const section = document.getElementById(id);
                  if (section.style.display === "none") {{
                    section.style.display = "block";
                    section.scrollIntoView({{ behavior: "smooth", block: "start" }});
                  }} else {{
                    section.style.display = "none";
                  }}
                }}
                function collapseAll() {{
                  const sections = document.querySelectorAll('[id*="-collapse"]')
                  const state = localStorage.getItem("displayState")
                  sections.forEach(section => {{
                    if (state === "none") {{
                      section.style.display = "block"
                    }} else {{
                      section.style.display = "none"
                    }}
                  }})
                  localStorage.setItem("displayState", state === "none" ? "block" : "none")
                }}
                localStorage.setItem("displayState", "none")
              </script>
            </body>
          </html>
        '''

    @staticmethod
    def info_container(name, description, rows):
        return f'''
          <li class="resource">
            <div class="heading">
              <h2 style="cursor: pointer; width: 100%" onclick="collapseAll()">
                Información General
              </h2>
              <ul class="endpoints">
                <li class="endpoint">
                  <ul class="operations">
                    <li class="mint operation">
                      <div class="heading">
                        <h3>
                          <span>
                            <a id="name">
                              Nombre
                            </a>
                          </span>
                          <span class="path">
                            <a>
                              {name}
                            </a>
                          </span>
                        </h3>
                      </div>
                      <div class="content">
                        <div>
                          <h4>
                            <span id="description">
                              Descripción
                            </span>
                          </h4>
                          <div>
                            <p>
                              {description}
                            </p>
                          </div>
                          <br>
                        </div>
                        <form>
                          <table class="fullwidth">
                            <tbody class="bold">
                              {rows}
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
        '''

    @staticmethod
    def section_container(title, sections, id, classes):
        val = lambda x: '' if id == 'default' else x
        return f'''
          <li class="resource">
            <div class="heading">
              <div
                style="{val('cursor: pointer;')}"
                onclick="{val(f"collapseSection('{id}-collapse')")}"
              >
                <h2 style="width: 100%;">
                  {title}
                </h2>
              </div>
              <div id={val(f"'{id}-collapse'")} style="{val('display: none;')}">
                <ul class="endpoints">
                  <li class="endpoint">
                    <ul class="{classes} operations">
                      {sections}
                    </ul>
                  </li>
                </ul>
              </div>
            </div>
          </li>
        '''

    @staticmethod
    def section(headers, rows, classes):
        return f'''
          <li class="{classes} operation">
            <div class="content">
                <table style="table-layout: fixed; width: 100%;">
                  <thead>
                    <tr>
                      {headers}
                    </tr>
                  </thead>
                  <tbody>
                    {rows}
                  </tbody>
                </table>
            </div>
          </li>
        '''

    @staticmethod
    def table(rows):
        return f'<table class="subtable">{rows}</table>'

    @staticmethod
    def table_header(value):
        return f'<th>{value}</th>'

    @staticmethod
    def table_row(cells):
        return f'<tr>{cells}</tr>'

    @staticmethod
    def table_cell(value):
        return f'<td>{value}</td>'

    @staticmethod
    def table_cell_pg(value):
        return f'<td><p>{value}</p></td>'

    @staticmethod
    def ulist(items):
        return f'<ul>{items}</ul>'

    @staticmethod
    def list_item(value):
        return f'<li>{value}</li>'
