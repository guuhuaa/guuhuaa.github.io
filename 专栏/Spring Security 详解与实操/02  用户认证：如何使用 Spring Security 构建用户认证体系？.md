<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>02  用户认证：如何使用 Spring Security 构建用户认证体系？.md</title>
        <!-- Spectre.css framework -->
        <link rel="stylesheet" href="../../static/index.css">
        <!-- theme css & js -->
        <meta name="generator" content="Hexo 4.2.0">
    </head>

<body>

<div class="book-container">
    <div class="book-sidebar">
        <div class="book-brand">
            <a href="../../index.html">
                <img src="../../static/favicon.png">
                <span>技术文章摘抄</span>
            </a>
        </div>
        <div class="book-menu uncollapsible">
            <ul class="uncollapsible">
                <li><a href="../../index.html" class="current-tab">首页</a></li>
            </ul>

            <ul class="uncollapsible">
                <li><a href="../index.html">上一级</a></li>
            </ul>

            <ul class="uncollapsible">
                <li>

                    
                    <a href="00&#32;开篇词&#32;&#32;Spring&#32;Security，为你的应用安全与职业之路保驾护航.md">00 开篇词  Spring Security，为你的应用安全与职业之路保驾护航.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;顶级框架：Spring&#32;Security&#32;是一款什么样的安全性框架？.md">01  顶级框架：Spring Security 是一款什么样的安全性框架？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="02&#32;&#32;用户认证：如何使用&#32;Spring&#32;Security&#32;构建用户认证体系？.md">02  用户认证：如何使用 Spring Security 构建用户认证体系？.md</a>
                    

                </li>
                <li>

                    
                    <a href="03&#32;&#32;认证体系：如何深入理解&#32;Spring&#32;Security&#32;用户认证机制？.md">03  认证体系：如何深入理解 Spring Security 用户认证机制？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;密码安全：Spring&#32;Security&#32;中包含哪些加解密技术？.md">04  密码安全：Spring Security 中包含哪些加解密技术？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;访问授权：如何对请求的安全访问过程进行有效配置？.md">05  访问授权：如何对请求的安全访问过程进行有效配置？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;权限管理：如何剖析&#32;Spring&#32;Security&#32;的授权原理？.md">06  权限管理：如何剖析 Spring Security 的授权原理？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;案例实战：使用&#32;Spring&#32;Security&#32;基础功能保护&#32;Web&#32;应用.md">07  案例实战：使用 Spring Security 基础功能保护 Web 应用.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;管道过滤：如何基于&#32;Spring&#32;Security&#32;过滤器扩展安全性？.md">08  管道过滤：如何基于 Spring Security 过滤器扩展安全性？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;攻击应对：如何实现&#32;CSRF&#32;保护和跨域&#32;CORS？.md">09  攻击应对：如何实现 CSRF 保护和跨域 CORS？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;全局方法：如何确保方法级别的安全访问？.md">10  全局方法：如何确保方法级别的安全访问？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;案例实战：使用&#32;Spring&#32;Security&#32;高级主题保护&#32;Web&#32;应用.md">11  案例实战：使用 Spring Security 高级主题保护 Web 应用.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;开放协议：OAuth2&#32;协议解决的是什么问题？.md">12  开放协议：OAuth2 协议解决的是什么问题？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;授权体系：如何构建&#32;OAuth2&#32;授权服务器？.md">13  授权体系：如何构建 OAuth2 授权服务器？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;资源保护：如何基于&#32;OAuth2&#32;协议配置授权过程？.md">14  资源保护：如何基于 OAuth2 协议配置授权过程？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;令牌扩展：如何使用&#32;JWT&#32;实现定制化&#32;Token？.md">15  令牌扩展：如何使用 JWT 实现定制化 Token？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;案例实战：基于&#32;Spring&#32;Security&#32;和&#32;Spring&#32;Cloud&#32;构建微服务安全架构.md">16  案例实战：基于 Spring Security 和 Spring Cloud 构建微服务安全架构.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;案例实战：基于&#32;Spring&#32;Security&#32;和&#32;OAuth2&#32;实现单点登录.md">17  案例实战：基于 Spring Security 和 OAuth2 实现单点登录.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;技术趋势：如何为&#32;Spring&#32;Security&#32;添加响应式编程特性？.md">18  技术趋势：如何为 Spring Security 添加响应式编程特性？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;测试驱动：如何基于&#32;Spring&#32;Security&#32;测试系统安全性？.md">19  测试驱动：如何基于 Spring Security 测试系统安全性？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;结束语&#32;&#32;以终为始，Spring&#32;Security&#32;的学习总结.md">20 结束语  以终为始，Spring Security 的学习总结.md</a>

                </li>
            </ul>

        </div>
    </div>

    <div class="sidebar-toggle" onclick="sidebar_toggle()" onmouseover="add_inner()" onmouseleave="remove_inner()">
        <div class="sidebar-toggle-inner"></div>
    </div>

    <script>
        function add_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.add('show')
        }

        function remove_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.remove('show')
        }

        function sidebar_toggle() {
            let sidebar_toggle = document.querySelector('.sidebar-toggle')
            let sidebar = document.querySelector('.book-sidebar')
            let content = document.querySelector('.off-canvas-content')
            if (sidebar_toggle.classList.contains('extend')) { // show
                sidebar_toggle.classList.remove('extend')
                sidebar.classList.remove('hide')
                content.classList.remove('extend')
            } else { // hide
                sidebar_toggle.classList.add('extend')
                sidebar.classList.add('hide')
                content.classList.add('extend')
            }
        }
    </script>

    <div class="off-canvas-content">
        <div class="columns">
            <div class="column col-12 col-lg-12">
                <div class="book-navbar">
                    <!-- For Responsive Layout -->
                    <header class="navbar">
                        <section class="navbar-section">
                            <a onclick="open_sidebar()">
                                <i class="icon icon-menu"></i>
                            </a>
                        </section>
                    </header>
                </div>
                <div class="book-content" style="max-width: 960px; margin: 0 auto;
    overflow-x: auto;
    overflow-y: hidden;">
                    <div class="book-post">
                        <p id="tip" align="center"></p>
                        <div><h1>02  用户认证：如何使用 Spring Security 构建用户认证体系？</h1>
<p>上一讲中，我们引入了 Spring Security 框架，并梳理了它的各项核心功能。从今天开始，我们就对这些功能一一展开讲解，首先要讨论的就是<strong>用户认证功能</strong>。用户认证涉及用户账户体系的构建，也是<strong>实现授权管理的前提</strong>。在 Spring Security 中，实现用户认证的方式有很多，下面我们就结合框架提供的配置体系进行梳理。</p>
<h3>Spring Security 配置体系</h3>
<p>在 Spring Security 中，因为认证和授权等功能通常都不止有一种实现方法，所以框架开发了一套完整的配置体系来对这些功能进行灵活设置。开发人员在使用认证和授权等功能时就依赖于如何合理利用和扩展这套配置体系。</p>
<p>例如，针对用户账户存储这个切入点，就可以设计出多种不同的策略。我们可以把用户名和密码保存在内存中，作为一种轻量级的实现方式。更常见的，也可以把这些认证信息存储在关系型数据库中。当然，如果我们使用了 LDAP 协议，那么文件系统也是一种不错的存储媒介。</p>
<p>显然，针对这些可选择的实现方式，需要为开发人员提供一种机制以便他们能够根据自身的需求进行灵活的设置，这就是配置体系的作用。</p>
<p>同时，你应该也注意到了，在上一讲的示例中，我们没有进行任何的配置也能让 Spring Security 发挥作用，这就说明框架内部的功能采用了<strong>特定的默认配置</strong>。就用户认证这一场景而言，Spring Security 内部就初始化了一个默认的用户名“user”并且在应用程序启动时自动生成一个密码。当然，通过这种方式自动生成的密码在每次启动应用时都会发生变化，并不适合面向正式的应用。</p>
<p>我们可以通过翻阅框架的源代码（<a href="https://github.com/spring-projects/spring-security?fileGuid=xxQTRXtVcqtHK6j8">https://github.com/spring-projects/spring-security</a>）来进一步理解 Spring Security 中的一些默认配置。在 Spring Security 中，初始化用户信息依赖的配置类是 WebSecurityConfigurer 接口，该接口实际上是一个空接口，继承了更为基础的 SecurityConfigurer 接口。</p>
<p>在日常开发中，通常不需要我们自己实现这个接口，而是<strong>使用 WebSecurityConfigurerAdapter 类</strong>来简化该配置类的使用方式。而在 WebSecurityConfigurerAdapter 中我们发现了如下所示的 configure 方法：</p>
<pre><code>protected void configure(HttpSecurity http) throws Exception {

 

        http

           .authorizeRequests()

               .anyRequest().authenticated()

               .and()

           .formLogin().and()

           .httpBasic();

}
</code></pre>
<p>上述代码就是 Spring Security 中作用于用户认证和访问授权的默认实现，这里用到了多个常见的配置方法。再次回想上一讲中我们讲到的，一旦在代码类路径中引入 Spring Security 框架之后，访问任何端点时就会弹出一个登录界面用来完成用户认证。<strong>认证是授权的前置流程</strong>，认证结束之后就可以进入到授权环节。</p>
<p>结合这些配置方法，我们来简单分析一下这种默认效果是如何实现的：</p>
<ul>
<li>首先，通过 HttpSecurity 类的 authorizeRequests() 方法对所有访问 HTTP 端点的 HttpServletRequest 进行限制；</li>
<li>然后，anyRequest().authenticated() 语句指定了对于所有请求都需要执行认证，也就是说没有通过认证的用户就无法访问任何端点；</li>
<li>接着，formLogin() 语句用于指定使用表单登录作为认证方式，也就是会弹出一个登录界面；</li>
<li>最后，httpBasic() 语句表示可以使用 HTTP 基础认证（Basic Authentication）方法来完成认证。</li>
</ul>
<p>在日常开发过程中，我们可以继承 WebSecurityConfigurerAdapter 类并且覆写上述的 configure() 方法来完成配置工作。而在 Spring Security 中，存在一批类似于 WebSecurityConfigurerAdapter 的配置类。</p>
<p><strong>配置体系是开发人员使用 Spring Security 框架的主要手段之一</strong>，关于配置体系的讨论会贯穿我们整个专栏的始终。随着内容深度的演进，Spring Security 所提供的全面而灵活的配置功能也将一一展现在你的面前。</p>
<h3>实现 HTTP 基础认证和表单登录认证</h3>
<p>在上文中，我们提到了 httpBasic() 和 formLogin() 这两种用于控制用户认证的实现手段，分别代表了<strong>HTTP 基础认证和表单登录认证</strong>。在构建 Web 应用程序时，我们也可以在 Spring Security 提供的认证机制的基础上进行扩展，以满足日常开发需求。</p>
<h4>HTTP 基础认证</h4>
<p>HTTP 基础认证的原理比较简单，只需<strong>通过 HTTP 协议的消息头携带用户名和密码</strong>进行登录验证。在上一讲中，我们已经通过浏览器简单验证了用户登录操作。今天，我们将引入 Postman 这款可视化的 HTTP 请求工具来对登录的请求和响应过程做进一步分析。</p>
<p>在 Postman 中，我们直接访问<a href="http://localhost:8080/hello?fileGuid=xxQTRXtVcqtHK6j8">http://localhost:8080/hello</a>端点，会得到如下所示的响应：</p>
<pre><code>{

    &quot;timestamp&quot;: &quot;2021-02-08T03:45:21.512+00:00&quot;,

    &quot;status&quot;: 401,

    &quot;error&quot;: &quot;Unauthorized&quot;,

    &quot;message&quot;: &quot;&quot;,

    &quot;path&quot;: &quot;/hello&quot;

}
</code></pre>
<p>显然，响应码 401 告诉我们没有访问该地址的权限。同时，在响应中出现了一个“WWW-Authenticate”消息头，其值为“Basic realm=&quot;Realm&quot;”，这里的 Realm 表示 Web 服务器中受保护资源的安全域。</p>
<p>现在，让我们来执行 HTTP 基础认证，可以通过设置认证类型为“Basic Auth”并输入对应的用户名和密码来完成对 HTTP 端点的访问，设置界面如下所示：</p>
<p><img src="assets/CioPOWC5_duASv7jAACBgx8x8WU605.png" alt="Drawing 0.png" /></p>
<p>使用 Postman 完成 HTTP 基础认证信息的设置</p>
<p>现在查看 HTTP 请求，可以看到 Request Header 中添加了 <a href="https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Authorization?fileGuid=xxQTRXtVcqtHK6j8">Authorization</a> 标头，格式为：Authorization:<code> &lt;type&gt;</code> <code>&lt;credentials</code>&gt;。这里的 type 就是“Basic”，而 credentials 则是这样一个字符串：</p>
<pre><code>dXNlcjo5YjE5MWMwNC1lNWMzLTQ0YzctOGE3ZS0yNWNkMjY3MmVmMzk=
</code></pre>
<p>这个字符串就是<strong>将用户名和密码组合在一起，再经过 Base64 编码得到的结果</strong>。而我们知道 Base64 只是一种编码方式，并没有集成加密机制，所以本质上传输的还是<strong>明文形式</strong>。</p>
<p>当然，想要在应用程序中启用 HTTP 基础认证还是比较简单的，只需要在 WebSecurityConfigurerAdapter 的 configure 方法中添加如下配置即可：</p>
<pre><code>protected void configure(HttpSecurity http) throws Exception {

 

        http.httpBasic();

}
</code></pre>
<p>HTTP 基础认证比较简单，没有定制的登录页面，所以单独使用的场景比较有限。在使用 Spring Security 时，我们<strong>一般会把 HTTP 基础认证和接下来要介绍的表单登录认证结合起来</strong>一起使用。</p>
<h4>表单登录认证</h4>
<p>在 WebSecurityConfigurerAdapter 的 configure() 方法中，一旦配置了 HttpSecurity 的 formLogin() 方法，就启动了表单登录认证，如下所示：</p>
<pre><code>protected void configure(HttpSecurity http) throws Exception {

 

        http.formLogin();

}
</code></pre>
<p>formLogin() 方法的执行效果就是提供了一个默认的登录界面，如下所示：</p>
<p><img src="assets/CioPOWC5_fmAOso9AAAqvMlklW8869.png" alt="Drawing 1.png" /></p>
<p>Spring Security 默认的登录界面</p>
<p>我们已经在上一讲中看到过这个登录界面。对于登录操作而言，这个登录界面通常都是定制化的，同时，我们也需要对登录的过程和结果进行细化控制。此时，我们就可以通过如下所示的配置内容来修改系统的默认配置：</p>
<pre><code>@Override

protected void configure(HttpSecurity http) throws Exception {

	 

    http

        .formLogin()        

        .loginPage(&quot;/login.html&quot;)//自定义登录页面

        .loginProcessingUrl(&quot;/action&quot;)//登录表单提交时的处理地址

        .defaultSuccessUrl(&quot;/index&quot;);//登录认证成功后的跳转页面        

}
</code></pre>
<p>可以看到，这里我们对登录界面、登录请求处理地址以及登录成功后的跳转界面进行了定制化。</p>
<h3>配置 Spring Security 用户认证体系</h3>
<p>讲完配置体系，现在让我们回到用户认证场景。因为 Spring Security 默认提供的用户名是固定的，而密码会随着每次应用程序的启动而变化，所以很不灵活。在 Spring Boot 中，我们可以通过在 application.yml 配置文件中添加如下所示的配置项来改变这种默认行为：</p>
<pre><code>spring:

  security:

    user:

      name: spring

      password: spring_password
</code></pre>
<p>现在让我们重启应用，就可以使用上述用户名和密码完成登录。基于配置文件的用户信息存储方案简单直接，但显然也<strong>缺乏灵活性</strong>，因为我们无法在系统运行时<strong>动态加载对应的用户名和密码</strong>。因此，在现实中，我们主要还是通过使用 WebSecurityConfigurerAdapter 配置类来改变默认的配置行为。</p>
<p>通过前面的内容中，我们已经知道可以通过 WebSecurityConfigurerAdapter 类的 configure(HttpSecurity http) 方法来完成认证。认证过程涉及 Spring Security 中用户信息的交互，我们可以通过继承 WebSecurityConfigurerAdapter 类并且覆写其中的 configure(AuthenticationManagerBuilder auth) 的方法来完成对用户信息的配置工作。请注意<strong>这是两个不同的 configure() 方法</strong>。</p>
<p>针对 WebSecurityConfigurer 配置类，我们首先需要明确配置的内容。实际上，初始化用户信息非常简单，只需要指定用户名（Username）、密码（Password）和角色（Role）这三项数据即可。在 Spring Security 中，基于 AuthenticationManagerBuilder 工具类为开发人员提供了<strong>基于内存、JDBC、LDAP 等多种验证方案</strong>。</p>
<p>接下来，我们就围绕 AuthenticationManagerBuilder 提供的功能来实现多种用户信息存储方案。</p>
<h4>使用基于内存的用户信息存储方案</h4>
<p>我们先来看如何使用 AuthenticationManagerBuilder 完成基于内存的用户信息存储方案。实现方法就是调用 AuthenticationManagerBuilder 的 inMemoryAuthentication 方法，示例代码如下：</p>
<pre><code>@Override

protected void configure(AuthenticationManagerBuilder builder) throws Exception {

 

    builder.inMemoryAuthentication()

        .withUser(&quot;spring_user&quot;).password(&quot;password1&quot;).roles(&quot;USER&quot;)

        .and()

        .withUser(&quot;spring_admin&quot;).password(&quot;password2&quot;).roles(&quot;USER&quot;, &quot;ADMIN&quot;);

}
</code></pre>
<p>从上面的代码中，我们可以看到系统中存在“spring_user”和“spring_admin”这两个用户，其密码分别是&quot;password1&quot;和&quot;password2&quot;，在角色上也分别代表着普通用户 USER 以及管理员 ADMIN。</p>
<p>请注意，这里的 roles() 方法背后使用的还是<strong>authorities() 方法</strong>。通过 roles() 方法，Spring Security 会在每个角色名称前自动添加“ROLE_”前缀，所以我们也可以通过如下所示的代码实现同样的功能：</p>
<pre><code>@Override

protected void configure(AuthenticationManagerBuilder builder) throws Exception {

 

    builder.inMemoryAuthentication()

         .withUser(&quot;spring_user&quot;).password(&quot;password1&quot;).authorities(&quot;ROLE_USER&quot;)

         .and()

         .withUser(&quot;spring_admin&quot;).password(&quot;password2&quot;).authorities(&quot;ROLE_USER&quot;, &quot;ROLE_ADMIN&quot;);

}
</code></pre>
<p>可以看到，基于内存的用户信息存储方案实现也比较简单，但同样缺乏灵活性，因为用户信息是写死在代码里的。所以，我们接下来就要引出另一种更为常见的用户信息存储方案——数据库存储。</p>
<h4>使用基于数据库的用户信息存储方案</h4>
<p>既然是将用户信息存储在数据库中，势必需要<strong>创建表结构</strong>。我们可以在 Spring Security 的源文件（org/springframework/security/core/userdetails/jdbc/users.ddl）中找到对应的 SQL 语句，如下所示：</p>
<pre><code>create table users(username varchar_ignorecase(50) not null primary key,password varchar_ignorecase(500) not null,enabled boolean not null);

 

create table authorities (username varchar_ignorecase(50) not null,authority varchar_ignorecase(50) not null,constraint fk_authorities_users foreign key(username) references users(username));

 

create unique index ix_auth_username on authorities (username,authority);
</code></pre>
<p>一旦我们在自己的数据库中创建了这两张表，并添加了相应的数据，就可以直接通过注入一个 DataSource 对象进行用户数据的查询，如下所示：</p>
<pre><code>@Autowired

DataSource dataSource;

 

@Override

protected void configure(AuthenticationManagerBuilder auth) throws Exception {

 

        auth.jdbcAuthentication().dataSource(dataSource)

               .usersByUsernameQuery(&quot;select username, password, enabled from Users &quot; + &quot;where username=?&quot;)

               .authoritiesByUsernameQuery(&quot;select username, authority from UserAuthorities &quot; + &quot;where username=?&quot;)

               .passwordEncoder(new BCryptPasswordEncoder());

}
</code></pre>
<p>这里使用了 AuthenticationManagerBuilder 的 jdbcAuthentication 方法来配置数据库认证方式，内部则使用了 JdbcUserDetailsManager 这个工具类。在该类中，就定义了各种用于数据库查询的 SQL 语句，以及使用 JdbcTemplate 完成数据库访问的具体实现方法。</p>
<p>请你注意，这里我们用到了一个<strong>passwordEncoder() 方法</strong>，这是 Spring Security 中提供的一个<strong>密码加解密器</strong>，我们会在“密码安全：Spring Security 中包含哪些加解密技术？”一讲中进行详细的讨论。</p>
<h3>小结与预告</h3>
<p>这一讲我们详细介绍了如何使用 Spring Security 构建用户认证体系的系统方法。在 Spring Security 中，认证相关的功能都是可以通过配置体系进行定制化开发和管理的。通过简单的配置方法，我们可以组合使用 HTTP 基础认证和表单登录认证，也可以分别基于内存以及基于数据库方案来存储用户信息，这些功能都是 Spring Security 内置的。</p>
<p>本讲内容总结如下：</p>
<p><img src="assets/CioPOWC5_g-AP68cAACSqF1r51g526.png" alt="Drawing 2.png" /></p>
<p>最后我想给你留一道思考题：你知道在 Spring Security 中有哪几种存储用户信息的实现方案吗？欢迎在留言区和我分享你的想法。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="01&#32;&#32;顶级框架：Spring&#32;Security&#32;是一款什么样的安全性框架？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="03&#32;&#32;认证体系：如何深入理解&#32;Spring&#32;Security&#32;用户认证机制？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434d800d5870ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
</body>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-NPSEEVD756"></script>
<script>
    window.dataLayer = window.dataLayer || [];

    function gtag() {
        dataLayer.push(arguments);
    }

    gtag('js', new Date());
    gtag('config', 'G-NPSEEVD756');
    var path = window.location.pathname
    var cookie = getCookie("lastPath");
    console.log(path)
    if (path.replace("/", "") === "") {
        if (cookie.replace("/", "") !== "") {
            console.log(cookie)
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Spring%20Security%20%E8%AF%A6%E8%A7%A3%E4%B8%8E%E5%AE%9E%E6%93%8D/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
        }
    } else {
        setCookie("lastPath", path)
    }

    function setCookie(cname, cvalue) {
        var d = new Date();
        d.setTime(d.getTime() + (180 * 24 * 60 * 60 * 1000));
        var expires = "expires=" + d.toGMTString();
        document.cookie = cname + "=" + cvalue + "; " + expires + ";path = /";
    }

    function getCookie(cname) {
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i].trim();
            if (c.indexOf(name) === 0) return c.substring(name.length, c.length);
        }
        return "";
    }
</script>

</html>
