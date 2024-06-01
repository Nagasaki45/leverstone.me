Phoenix, templates, and active navbar items
###########################################
:date: 2016-12-22 15:30
:author: Tom Gurion
:tags: tutorials, elixir, phoenix, web
:slug: phoenix-templates-and-active-navbar-items
:description: A short tutorial on setting the active navbar item dynamically with phoenix and bootstrap.

We build a web-app, and want the items on the navigation bar to be active when the user visits the corresponding page, like this:

.. image:: /images/blog/navbar_active_items.gif
  :width: 100%
  :alt: An animated example of active navigation bar items.

I'm not saying that this is a complicated task in other frameworks, but it often feels "hacky".
Here is a `phoenix`_ solution that feels pretty elegant, and therefore worth sharing.

So, let's start with a simple `twitter-bootstrap`_ navbar example for our web-app, with links to our home, products, and about pages.

.. code-block:: html

  <nav class="navbar navbar-default">
    <ul class="nav navbar-nav">
      <li><a href="#">Home</a></li>
      <li><a href="#">Products</a></li>
      <li><a href="#">About</a></li>
    </ul>
  </nav>

Right now, none of the links are highlighted.
We need to add a ``class="active"`` to the ``<li>`` item that corresponds to the current page.
The question is, how can we do it dynamically, according to the current visited page?

The |Plug.Conn|_ contains all of the information for the current request/response cycle, and is available in our views and template.
Moreover, the ``&Phoenix.Controller.action_name/1`` function expects a ``Plug.Conn`` and returns the name of the controller function that was used to process the request.
With this information in mind, let's create a template to render navbar ``<li>`` items.
First, we will have to make the ``action_name`` function available in our views.
Edit ``web/web.ex`` to import it to all of the views.

.. code-block:: diff

    # Import convenience functions from controllers
  - import Phoenix.Controller, only: [get_csrf_token: 0, get_flash: 2, view_module: 1]
  + import Phoenix.Controller, only: [get_csrf_token: 0, get_flash: 2, view_module: 1, action_name: 1]

Now we are ready to create the template for the navbar items:

.. code-block:: html

  <!-- web/templates/layout/navbar_item.html.eex -->

  <%= if action_name(@conn) == @action do %>
  <li class="active">
  <%= else %>
  <li>
  <%= end %>
    <%= link @text, to: page_path(@conn, @action) %>
  </li>

Notice that this template expects the ``conn``, ``action`` (as an atom), and ``text`` (for the link) as assigns.
It also uses the ``link`` function to create the ``<a>`` tags automatically by finding the path in the routing table for us.
We can already use it by replacing our previous navbar with:

.. code-block:: html

  <nav class="navbar navbar-default">
    <ul class="nav navbar-nav">
      <%= render "navbar_item.html", conn: @conn, action: :index, text: "Home" %>
      <%= render "navbar_item.html", conn: @conn, action: :products, text: "Products" %>
      <%= render "navbar_item.html", conn: @conn, action: :about, text: "About" %>
    </ul>
  </nav>

However, it is even more elegant and concise to add the following function to the layout view:

.. code-block:: elixir

  # web/views/layout_view.ex

  def navbar_item(assigns) do
    render "navbar_item.html", assigns
  end

And improve the navbar:

.. code-block:: html

  <nav class="navbar navbar-default">
    <ul class="nav navbar-nav">
      <%= navbar_item conn: @conn, action: :index, text: "Home" %>
      <%= navbar_item conn: @conn, action: :products, text: "Products" %>
      <%= navbar_item conn: @conn, action: :about, text: "About" %>
    </ul>
  </nav>

In addition to ``action_name``, you might also be interested in ``Phoenix.Controller.controller_module``, as suggested `here`_.
I hope that this short tutorial helped you.
Good luck with your navbar!

.. |Plug.Conn| replace:: ``Plug.Conn``
.. _`phoenix`: http://www.phoenixframework.org/
.. _`twitter-bootstrap`: https://getbootstrap.com/
.. _`Plug.Conn`: https://hexdocs.pm/plug/readme.html#the-plug-conn
.. _`here`: http://stackoverflow.com/a/36009443/1224456
