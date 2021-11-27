<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>18  用户认证：如何基于 Spring Security 构建用户认证体系？.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;从零开始：为什么要学习&#32;Spring&#32;Boot？.md">00 开篇词  从零开始：为什么要学习 Spring Boot？.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;家族生态：如何正确理解&#32;Spring&#32;家族的技术体系？.md">01  家族生态：如何正确理解 Spring 家族的技术体系？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;案例驱动：如何剖析一个&#32;Spring&#32;Web&#32;应用程序？.md">02  案例驱动：如何剖析一个 Spring Web 应用程序？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;多维配置：如何使用&#32;Spring&#32;Boot&#32;中的配置体系？.md">03  多维配置：如何使用 Spring Boot 中的配置体系？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;定制配置：如何创建和管理自定义的配置信息？.md">04  定制配置：如何创建和管理自定义的配置信息？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;自动配置：如何正确理解&#32;Spring&#32;Boot&#32;自动配置实现原理？.md">05  自动配置：如何正确理解 Spring Boot 自动配置实现原理？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;基础规范：如何理解&#32;JDBC&#32;关系型数据库访问规范？.md">06  基础规范：如何理解 JDBC 关系型数据库访问规范？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;数据访问：如何使用&#32;JdbcTemplate&#32;访问关系型数据库？.md">07  数据访问：如何使用 JdbcTemplate 访问关系型数据库？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;数据访问：如何剖析&#32;JdbcTemplate&#32;数据访问实现原理？.md">08  数据访问：如何剖析 JdbcTemplate 数据访问实现原理？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;数据抽象：Spring&#32;Data&#32;如何对数据访问过程进行统一抽象？.md">09  数据抽象：Spring Data 如何对数据访问过程进行统一抽象？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;ORM&#32;集成：如何使用&#32;Spring&#32;Data&#32;JPA&#32;访问关系型数据库？.md">10  ORM 集成：如何使用 Spring Data JPA 访问关系型数据库？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;服务发布：如何构建一个&#32;RESTful&#32;风格的&#32;Web&#32;服务？.md">11  服务发布：如何构建一个 RESTful 风格的 Web 服务？.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;服务调用：如何使用&#32;RestTemplate&#32;消费&#32;RESTful&#32;服务？.md">12  服务调用：如何使用 RestTemplate 消费 RESTful 服务？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;服务调用：如何正确理解&#32;RestTemplate&#32;远程调用实现原理？.md">13  服务调用：如何正确理解 RestTemplate 远程调用实现原理？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;消息驱动：如何使用&#32;KafkaTemplate&#32;集成&#32;Kafka？.md">14  消息驱动：如何使用 KafkaTemplate 集成 Kafka？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;消息驱动：如何使用&#32;JmsTemplate&#32;集成&#32;ActiveMQ？.md">15  消息驱动：如何使用 JmsTemplate 集成 ActiveMQ？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;消息驱动：如何使用&#32;RabbitTemplate&#32;集成&#32;RabbitMQ？.md">16  消息驱动：如何使用 RabbitTemplate 集成 RabbitMQ？.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;安全架构：如何理解&#32;Spring&#32;安全体系的整体架构？.md">17  安全架构：如何理解 Spring 安全体系的整体架构？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="18&#32;&#32;用户认证：如何基于&#32;Spring&#32;Security&#32;构建用户认证体系？.md">18  用户认证：如何基于 Spring Security 构建用户认证体系？.md</a>
                    

                </li>
                <li>

                    
                    <a href="19&#32;&#32;服务授权：如何基于&#32;Spring&#32;Security&#32;确保请求安全访问？.md">19  服务授权：如何基于 Spring Security 确保请求安全访问？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;服务监控：如何使用&#32;Actuator&#32;组件实现系统监控？.md">20  服务监控：如何使用 Actuator 组件实现系统监控？.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;指标定制：如何实现自定义度量指标和&#32;Actuator&#32;端点？.md">21  指标定制：如何实现自定义度量指标和 Actuator 端点？.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;运行管理：如何使用&#32;Admin&#32;Server&#32;管理&#32;Spring&#32;应用程序？.md">22  运行管理：如何使用 Admin Server 管理 Spring 应用程序？.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;数据测试：如何使用&#32;Spring&#32;测试数据访问层组件？.md">23  数据测试：如何使用 Spring 测试数据访问层组件？.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;服务测试：如何使用&#32;Spring&#32;测试&#32;Web&#32;服务层组件？.md">24  服务测试：如何使用 Spring 测试 Web 服务层组件？.md</a>

                </li>
                <li>

                    
                    <a href="结束语&#32;&#32;以终为始：Spring&#32;Boot&#32;总结和展望.md">结束语  以终为始：Spring Boot 总结和展望.md</a>

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
                        <div><h1>18  用户认证：如何基于 Spring Security 构建用户认证体系？</h1>
<p>在 17 讲中，我们梳理了 Web 应用程序的安全性需求，并引出了 Spring Security 这款 Spring 家族中专门用于处理安全性需求的开发框架，同时也明确了认证和授权是安全性框架的核心功能。</p>
<p>这一讲我们将先讨论与认证相关的话题，并给出 Spring Security 认证机制及其使用方法。因为 Spring Security 是日常开发过程中的基础组件，所以我们也会对如何实现数据加解密的过程做一些展开。</p>
<p>在 Spring Boot 中整合 Spring Security 框架的方式非常简单，我们只需要在 pom 文件中引入 spring-boot-starter-security 依赖即可，这与以往需要提供很多配置才能与 Spring Security 完成集成的开发过程不同，如下代码所示：</p>
<pre><code>&lt;dependency&gt;

    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;

    &lt;artifactId&gt;spring-boot-starter-security&lt;/artifactId&gt;

&lt;/dependency&gt;
</code></pre>
<hr />
<p><strong>请注意，只要我们在代码工程中添加了上述依赖，包含在该工程中的所有 HTTP 端点都将被保护起来。</strong></p>
<p>例如，在 SpringCSS 案例的 account-service 中，我们知道存在一个 AccountController ，且它暴露了一个“accounts/ /{accountId}”端点。现在，我们启动 account-service 服务并访问上述端点，弹出了如下图所示的界面内容：</p>
<p><img src="assets/CgqCHmABN02AZfgTAAAR0uEiE5U744.png" alt="Drawing 0.png" /></p>
<p>添加 Spring Security 之后自动出现的登录界面</p>
<p>同时，在系统的启动控制台日志中，我们发现了如下所示的新的日志信息。</p>
<pre><code>Using generated security password: 17bbf7c4-456a-48f5-a12e-a680066c8f80
</code></pre>
<p>在这里可以看到，Spring Security 为我们自动生成了一个密码，我们可以基于“user”这个账号及上述密码登录这个界面，抽空你也可以尝试下。</p>
<p>如果我们使用了 Postman 可视化 HTTP 请求工具，可以设置授权类型为“Basic Auth”并输入对应的用户名和密码完成对 HTTP 端点的访问，设置界面如下图所示：</p>
<p><img src="assets/CgqCHmABN1uAC5vsAAA3VhGEBJY812.png" alt="Drawing 1.png" /></p>
<p>使用 Postman 来完成认证信息的设置</p>
<p>事实上，在引入 spring-boot-starter-security 依赖之后，Spring Security 会默认创建一个用户名为“user”的账号。很显然，每次启动应用时，通过 Spring Security 自动生成的密码都会有所变化，因此它不适合作为一种正式的应用方法。</p>
<p>如果我们想设置登录账号和密码，最简单的方式是通过配置文件。例如，我们可以在 account-service 的 application.yml 文件中添加如下代码所示的配置项：</p>
<pre><code>spring:

  security:

    user:

      name: springcss

      password: springcss_password
</code></pre>
<p>重启 account-service 服务后，我们就可以使用上述用户名和密码完成登录。</p>
<p>虽然基于配置文件的用户信息存储方案简单且直接，但是显然缺乏灵活性，因此 Spring Security 为我们提供了多种存储和管理用户认证信息的方案，我们一起来看一下。</p>
<h3>配置 Spring Security</h3>
<p>在 SpringSecurity 中，初始化用户信息所依赖的配置类是 WebSecurityConfigurer 接口，该接口实际上是一个空接口，继承了更为基础的 SecurityConfigurer 接口。</p>
<p>在日常开发中，我们往往不需要自己实现这个接口，而是使用 WebSecurityConfigurerAdapter 类简化该配置类的使用方式。比如我们可以通过继承 WebSecurityConfigurerAdapter 类并且覆写其中的 configure(AuthenticationManagerBuilder auth) 的方法完成配置工作。</p>
<p>关于 WebSecurityConfigurer 配置类，首先我们需要明确配置的内容。实际上，初始化所使用的用户信息非常简单，只需要指定用户名（Username）、密码（Password）和角色（Role）这三项数据即可。</p>
<p>在 WebSecurityConfigurer 类中，使用 AuthenticationManagerBuilder 类创建一个 AuthenticationManager 就能够轻松实现基于内存、LADP 和 JDBC 的验证。</p>
<p>接下来，我们就围绕 AuthenticationManagerBuilder 提供的功能实现多种用户信息存储方案。</p>
<h4>使用基于内存的用户信息存储方案</h4>
<p>我们先来看看如何使用 AuthenticationManagerBuilder 完成基于内存的用户信息存储方案。</p>
<p>实现方法是调用 AuthenticationManagerBuilder 的 inMemoryAuthentication 方法，示例代码如下所示：</p>
<pre><code>@Override

protected void configure(AuthenticationManagerBuilder builder) throws Exception {

 

        builder.inMemoryAuthentication()

                .withUser(&quot;springcss_user&quot;).password(&quot;password1&quot;)

	.roles(&quot;USER&quot;)

                .and()

                .withUser(&quot;springcss_admin&quot;).password(&quot;password2&quot;)

	.roles(&quot;USER&quot;, &quot;ADMIN&quot;);

}
</code></pre>
<p>从上面的代码中，我们看到系统中存在&quot;springcss _user&quot;和&quot;springcss _admin&quot;这两个用户，其密码分别是&quot;password1&quot;和&quot;password2&quot;，分别代表着普通用户 USER 及管理员 ADMIN 这两个角色。</p>
<p>在 AuthenticationManagerBuilder 中，上述 inMemoryAuthentication 的方法的实现过程如下代码所示：</p>
<pre><code>public InMemoryUserDetailsManagerConfigurer&lt;AuthenticationManagerBuilder&gt; inMemoryAuthentication()

            throws Exception {

        return apply(new InMemoryUserDetailsManagerConfigurer&lt;&gt;());

}
</code></pre>
<p>这里的 InMemoryUserDetailsManagerConfigurer 内部又使用到了 InMemoryUserDetailsManager 对象，而通过深入该类，我们可以获取 Spring Security 中与用户认证相关的一大批核心对象，它们之间的关系如下图所示：</p>
<p><img src="assets/Cip5yGABYdOAHvU6AADbh8te5-8316.png" alt="图片3" /></p>
<p>Spring Security 中用户认证相关类结构图</p>
<p>首先，我们来看上图中代表用户详细信息的 UserDetails 接口，如下代码所示：</p>
<pre><code>public interface UserDetails extends Serializable {

    //获取该用户的权限信息

    Collection&lt;? extends GrantedAuthority&gt; getAuthorities();

    //获取密码

	String getPassword();

	//获取用户名

    String getUsername();

	//判断该账户是否已失效

    boolean isAccountNonExpired();

    //判断该账户是否已被锁定

    boolean isAccountNonLocked();

    //判断该账户的凭证信息是否已失效

    boolean isCredentialsNonExpired();

    //判断该用户是否可用

    boolean isEnabled();

}
</code></pre>
<p>在上述代码中，我们发现 UserDetails 存在一个子接口 MutableUserDetails，从命名上不难看出，后者是一个可变的 UserDetails，而可变的内容就是密码。</p>
<p>关于 MutableUserDetails 接口的定义如下代码所示：</p>
<pre><code>interface MutableUserDetails extends UserDetails {

    //设置密码

    void setPassword(String password);

}
</code></pre>
<p>在 Spring Security 中，针对 UserDetails 还存在一个专门的 UserDetailsService，该接口专门用来管理 UserDetails，它的定义如下代码所示：</p>
<pre><code>public interface UserDetailsService {

    //根据用户名获取用户信息

    UserDetails loadUserByUsername(String username) throws UsernameNotFoundException;

}
</code></pre>
<p>而 UserDetailsManager 继承了 UserDetailsService，并提供了一批针对 UserDetails 的操作接口，如下代码所示：</p>
<pre><code>public interface UserDetailsManager extends UserDetailsService {

    //创建用户

    void createUser(UserDetails user);

    //更新用户

    void updateUser(UserDetails user);

    //删除用户

    void deleteUser(String username);

    //修改密码

    void changePassword(String oldPassword, String newPassword);

    //判断指定用户名的用户是否存在

    boolean userExists(String username);

}
</code></pre>
<p>介绍完 UserDetailsManager 后，我们再回到 InMemoryUserDetailsManager 类，它实现了 UserDetailsManager 接口中的所有方法，这些方法主要用来对用户信息进行维护，从而形成一条代码支线。</p>
<p>为了完成用户信息的配置，还存在另外一条代码支线，即 UserDetailsManagerConfigurer。该类维护了一个 UserDetails 列表，并提供了一组 withUser 方法完成用户信息的初始化，如下代码所示：</p>
<pre><code>private final List&lt;UserDetails&gt; users = new ArrayList&lt;&gt;();

 

public final C withUser(UserDetails userDetails) {

        this.users.add(userDetails);

        return (C) this;

}
</code></pre>
<p>从上述代码中，我们看到 withUser 方法返回的是一个 UserDetailsBuilder 对象，通过该对象可以实现类似 .withUser(&quot;springcss_user&quot;).password(&quot;password1&quot;).roles(&quot;USER&quot;) 这样的链式语法，从而完成用户信息的设置。</p>
<p><strong>请注意，这里的 .roles() 方法实际上是 .authorities() 方法的一种简写，因为 Spring Security 会在每个角色名称前自动添加“ROLE_”前缀</strong>，我们可以通过如下所示的代码实现同样的功能：</p>
<pre><code>@Override

protected void configure(AuthenticationManagerBuilder builder) throws Exception {

 

        builder.inMemoryAuthentication()

                .withUser(&quot;springcss_user&quot;).password(&quot;password1&quot;)

	.authorities(&quot;ROLE_USER&quot;)

                .and()

                .withUser(&quot;springcss_admin&quot;).password(&quot;password2&quot;)

	.authorities(&quot;ROLE_USER&quot;, &quot;ROLE_ADMIN&quot;);

}
</code></pre>
<p>我们可以看到，基于内存的用户信息存储方案也比较简单，但是由于用户信息写死在代码中，因此同样缺乏灵活性。</p>
<p>接下来我们将引出另一种更为常见的用户信息存储方案——数据库存储。</p>
<h4>使用基于数据库的用户信息存储方案</h4>
<p>既然是将用户信息存储在数据库中，我们势必需要创建表结构。因此，在 Spring Security 的源文件中，我们可以找到对应的 SQL 语句，如下代码所示：</p>
<pre><code>create table users(username varchar_ignorecase(50) not null primary key,password varchar_ignorecase(500) not null,enabled boolean not null);

 

create table authorities (username varchar_ignorecase(50) not null,authority varchar_ignorecase(50) not null,constraint fk_authorities_users foreign key(username) references users(username));

 

create unique index ix_auth_username on authorities (username,authority);
</code></pre>
<p>一旦在自己的数据库中创建了这两张表，且添加了相应数据，我们就可以直接注入一个 DataSource 对象查询用户数据，如下代码所示：</p>
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
<p>这里使用了 AuthenticationManagerBuilder 的 jdbcAuthentication 方法配置数据库认证方式，而内部则使用了 JdbcUserDetailsManager 工具类。</p>
<p>围绕 JdbcUserDetailsManager 整条代码链路的类层结构与 InMemoryUserDetailsManager 非常一致，在该类中定义了各种用户数据库查询的 SQL 语句，以及使用 JdbcTemplate 完成数据库访问的具体实现方法。这里我们不再具体展开，你可以对照前面给出的 InMemoryUserDetailsManager 类层结构图进行分析。</p>
<hr />
<p><strong>注意，在上述方法中，通过 jdbcAuthentication() 方法验证用户信息时，我们必须集成加密机制，即使用 passwordEncoder() 方法嵌入一个 PasswordEncoder 接口的实现类。</strong></p>
<p>在 Spring Security 中，PasswordEncoder 接口代表一种密码编码器，定义如下代码所示：</p>
<pre><code>public interface PasswordEncoder {

    //对原始密码进行编码

    String encode(CharSequence rawPassword);

    //对提交的原始密码与库中存储的加密密码进行比对

    boolean matches(CharSequence rawPassword, String encodedPassword);

    //判断加密密码是否需要再次进行加密，默认返回false

    default boolean upgradeEncoding(String encodedPassword) {

        return false;

    }

}
</code></pre>
<p>Spring Security 中内置了一大批 PasswordEncoder 接口的实现类，如下图所示：</p>
<p><img src="assets/CgqCHmABN4qACniMAAB2uCwQA6M741.png" alt="Drawing 3.png" /></p>
<p>Spring Security 中的 PasswordEncoder 实现类</p>
<p>上图中，比较常用的算法如 SHA-256 算法的 StandardPasswordEncoder、bcrypt 强哈希算法的 BCryptPasswordEncoder 等。而在实际案例中，我们使用的是 BCryptPasswordEncoder，它的 encode 方法如下代码所示：</p>
<pre><code>public String encode(CharSequence rawPassword) {

        String salt;

        if (random != null) {

            salt = BCrypt.gensalt(version.getVersion(), strength, random);

        } else {

            salt = BCrypt.gensalt(version.getVersion(), strength);

        }

        return BCrypt.hashpw(rawPassword.toString(), salt);

}
</code></pre>
<p>可以看到，上述 encode 方法执行了两个步骤，第一步是生成盐，第二步是根据盐和明文密码生成最终的密文密码。</p>
<h3>实现定制化用户认证方案</h3>
<p>通过前面内容的分析，我们明确了用户信息存储的实现过程实际上是完全可定制化，而 Spring Security 所做的工作只是把常见、符合一般业务场景的实现方式嵌入框架中。如果存在特殊的场景，开发人员完全可以通过自定义用户信息存储方案进行实现。</p>
<p>在前面的内容中，我们介绍了 UserDetails 接口代表用户详细信息，而 UserDetailsService 接口负责对 UserDetails 进行各种操作 。因此，实现定制化用户认证方案的关键是实现 UserDetails 和 UserDetailsService 这两个接口。</p>
<h4>扩展 UserDetails</h4>
<p>扩展 UserDetails 的方法的实质是直接实现该接口，例如我们可以构建如下所示的 SpringCssUser 类：</p>
<pre><code>public class SpringCssUser implements UserDetails {

 

  private static final long serialVersionUID = 1L;

  private Long id;

  private final String username;

  private final String password;

  private final String phoneNumber;

  //省略getter/setter

    @Override

    public String getUsername() {

        return username;

    }

    @Override

    public String getPassword() {

        return password;

    }

 

  @Override

  public Collection&lt;? extends GrantedAuthority&gt; getAuthorities() {

    return Arrays.asList(new SimpleGrantedAuthority(&quot;ROLE_USER&quot;));

  }

 

  @Override

  public boolean isAccountNonExpired() {

    return true;

  }

 

  @Override

  public boolean isAccountNonLocked() {

    return true;

  }

 

  @Override

  public boolean isCredentialsNonExpired() {

    return true;

  }

 

  @Override

  public boolean isEnabled() {

    return true;

  }

}
</code></pre>
<p>显然，这里我们使用了一种更简单的方法满足 UserDetails 中各个接口的实现需求。一旦我们构建了一个 SpringCssUser 类，就可以创建对应的表结构存储类中所定义的字段。同时，我们也可以基于 Spring Data JPA 创建一个自定义的 Repository，如下代码所示：</p>
<pre><code>public interface SpringCssUserRepository extends CrudRepository&lt;SpringCssUser, Long&gt; {

    SpringCssUser findByUsername(String username);

}
</code></pre>
<p>SpringCssUserRepository 扩展了 CrudRepository 接口，并提供了一个方法名衍生查询 findByUsername。</p>
<p>关于 Spring Data JPA 的使用方法，你还可以回顾《ORM 集成：如何使用 Spring Data JPA 访问关系型数据库？》。</p>
<h4>扩展 UserDetailsService</h4>
<p>接着，我们来实现 UserDetailsService 接口，如下代码所示：</p>
<pre><code>@Service

public class SpringCssUserDetailsService 

        implements UserDetailsService {

	 

	@Autowired

  private SpringCssUserRepository repository;

 

  @Override

  public UserDetails loadUserByUsername(String username)

      throws UsernameNotFoundException {

    SpringCssUser user = repository.findByUsername(username);

    if (user != null) {

      return user;

    }

    throw new UsernameNotFoundException(

                    &quot;SpringCSS User '&quot; + username + &quot;' not found&quot;);

  }

}
</code></pre>
<p>在 UserDetailsService 接口中，我们只需要实现 loadUserByUsername 方法就行。因此，我们可以基于 SpringCssUserRepository 的 findByUsername 方法，再根据用户名从数据库中查询数据。</p>
<h4>整合定制化配置</h4>
<p>最后，我们再次回到 SpringCssSecurityConfig 类。</p>
<p>这次我们将使用自定义的 SpringCssUserDetailsService 完成用户信息的存储和查询，此时我们只需要对配置策略做一些调整，调整后的完整 SpringCssSecurityConfig 类如下代码所示：</p>
<pre><code>@Configuration

public class SpringCssSecurityConfig extends WebSecurityConfigurerAdapter {

 

 

    @Autowired

    SpringCssUserDetailsService springCssUserDetailsService;

 

    @Override

    protected void configure(AuthenticationManagerBuilder auth) throws Exception {

 

     auth.userDetailsService(springCssUserDetailsService);

	}

}
</code></pre>
<p>这里我们注入了 SpringCssUserDetailsService，并将其添加到 AuthenticationManagerBuilder 中，这样 AuthenticationManagerBuilder 将基于自定义的 SpringCssUserDetailsService 完成 UserDetails 的创建和管理。</p>
<h3>小结与预告</h3>
<p>这一讲我们详细介绍了如何使用 Spring Security 构建用户认证体系的系统方法。</p>
<p>一方面，我们可以分别基于内存和数据库方案存储用户信息，这两种方案都是 Spring Security 内置的。另一方面，我们可以通过扩展 UserDetails 接口的方式实现定制化用户的认证方案。同时，为了方便你理解和掌握这部分内容，我们还梳理了与用户认证相关的核心类。</p>
<p>介绍完用户认证信息后，19 讲我们将介绍如何基于 Spring Security 确保 Web 请求的安全访问。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="17&#32;&#32;安全架构：如何理解&#32;Spring&#32;安全体系的整体架构？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="19&#32;&#32;服务授权：如何基于&#32;Spring&#32;Security&#32;确保请求安全访问？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434d46b87c70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Spring%20Boot%20%E5%AE%9E%E6%88%98%E5%BC%80%E5%8F%91/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
