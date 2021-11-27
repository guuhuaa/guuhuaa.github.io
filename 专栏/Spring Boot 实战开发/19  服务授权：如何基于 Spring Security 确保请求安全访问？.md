<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>19  服务授权：如何基于 Spring Security 确保请求安全访问？.md</title>
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

                    
                    <a href="18&#32;&#32;用户认证：如何基于&#32;Spring&#32;Security&#32;构建用户认证体系？.md">18  用户认证：如何基于 Spring Security 构建用户认证体系？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="19&#32;&#32;服务授权：如何基于&#32;Spring&#32;Security&#32;确保请求安全访问？.md">19  服务授权：如何基于 Spring Security 确保请求安全访问？.md</a>
                    

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
                        <div><h1>19  服务授权：如何基于 Spring Security 确保请求安全访问？</h1>
<p>18 讲中，我们集中讨论了如何通过 WebSecurityConfigurerAdapter 完成对用户认证体系的构建。这一讲我们将继续使用这个配置类完成对服务访问的授权控制。</p>
<p>在日常开发过程中，我们需要对 Web 应用中的不同 HTTP 端点进行不同粒度的权限控制，并且希望这种控制方法足够灵活。而借助 Spring Security 框架，我们就可以对其进行简单实现，下面我们一起来看下。</p>
<h3>对 HTTP 端点进行访问授权管理</h3>
<p>在一个 Web 应用中，权限管理的对象是通过 Controller 层暴露的一个个 HTTP 端点，而这些 HTTP 端点就是需要授权访问的资源。</p>
<p>开发人员使用 Spring Security 中提供的一系列丰富技术组件，即可通过简单的设置对权限进行灵活管理。</p>
<h4>使用配置方法</h4>
<p>实现访问授权的第一种方法是使用配置方法，关于配置方法的处理过程也是位于 WebSecurityConfigurerAdapter 类中，但使用的是 configure(HttpSecurity http) 方法，如下代码所示：</p>
<pre><code>protected void configure(HttpSecurity http) throws Exception {

 

        http

            .authorizeRequests()

            .anyRequest()

            .authenticated()

            .and()

            .formLogin()

            .and()

            .httpBasic();

}
</code></pre>
<p>上述代码就是 Spring Security 中作用于访问授权的默认实现方法，这里用到了多个常见的配置方法。</p>
<p>回想 18 课时中的内容，访问任何端点时，一旦在代码类路径中引入了 Spring Security 框架，就会弹出一个登录界面从而完成用户认证。因为认证是授权的前置流程，认证结束后就可以进入授权环节。</p>
<p>结合这些配置方法的名称，我们简单分析一下实现这种默认的授权效果的具体步骤。</p>
<p>首先，通过 HttpSecurity 类的 authorizeRequests() 方法，我们可以对所有访问 HTTP 端点的 HttpServletRequest 进行限制。</p>
<p>其次，anyRequest().authenticated() 语句指定了所有请求都需要执行认证，也就是说没有通过认证的用户无法访问任何端点。</p>
<p>然后，formLogin() 语句指定了用户需要使用表单进行登录，即会弹出一个登录界面。</p>
<p>最后， httpBasic() 语句使用 HTTP 协议中的 Basic Authentication 方法完成认证。</p>
<p>18 讲中我们也演示了如何使用 Postman 完成认证的方式，这里就不过多赘述了。</p>
<p>当然，Spring Security 中还提供了很多其他有用的配置方法供开发人员灵活使用，下表中我们进行了列举，一起来看下。</p>
<p><img src="assets/CgpVE2AGpjqARlFfAAE9RHgwruA457.png" alt="Lark20210119-172757.png" /></p>
<p><strong>基于上表中的配置方法，我们就可以通过 HttpSecurity 实现自定义的授权策略。</strong></p>
<p>比方说，我们希望针对“/orders”根路径下的所有端点进行访问控制，且只允许认证通过的用户访问，那么可以创建一个继承了 WebSecurityConfigurerAdapter 类的 SpringCssSecurityConfig，并覆写其中的 configure(HttpSecurity http) 方法来实现，如下代码所示：</p>
<pre><code>@Configuration

public class SecurityConfig extends WebSecurityConfigurerAdapter {

 

    @Override

    public void configure(HttpSecurity http) throws Exception {

 

        http.authorizeRequests()

            .antMatchers(&quot;/orders/**&quot;)

            .authenticated();

    }

}
</code></pre>
<p><strong>请注意：虽然上表中的这些配置方法非常有用，但是由于我们无法基于一些来自环境和业务的参数灵活控制访问规则，也就存在一定的局限性。</strong></p>
<p>为此，Spring Security 还提供了一个 access() 方法，该方法允许开发人员传入一个表达式进行更细粒度的权限控制，这里，我们将引入Spring 框架提供的一种动态表达式语言—— SpEL（Spring Expression Language 的简称）。</p>
<p>只要 SpEL 表达式的返回值为 true，access() 方法就允许用户访问，如下代码所示：</p>
<pre><code>@Override

public void configure(HttpSecurity http) throws Exception {

 

        http.authorizeRequests()

            .antMatchers(&quot;/orders&quot;)

            .access(&quot;hasRole('ROLE_USER')&quot;);

}
</code></pre>
<p>上述代码中，假设访问“/orders”端点的请求必须具备“ROLE_USER”角色，通过 access 方法中的 hasRole 方法我们即可灵活地实现这个需求。当然，除了使用 hasRole 外，我们还可以使用 authentication、isAnonymous、isAuthenticated、permitAll 等表达式进行实现。因这些表达式的作用与前面介绍的配置方法一致，我们就不过多赘述。</p>
<h4>使用注解</h4>
<p>除了使用配置方法，Spring Security 还为我们提供了 @PreAuthorize 注解实现类似的效果，该注解定义如下代码所示：</p>
<pre><code>@Target({ ElementType.METHOD, ElementType.TYPE })

@Retention(RetentionPolicy.RUNTIME)

@Inherited

@Documented

public @interface PreAuthorize {

 

    //通过 SpEL 表达式设置访问控制

    String value();

}
</code></pre>
<p>可以看到 @PreAuthorize 的原理与前面介绍的 access() 方法一样，即通过传入一个 SpEL 表达式设置访问控制，如下所示代码就是一个典型的使用示例：</p>
<pre><code>@RestController

@RequestMapping(value=&quot;orders&quot;)

public class OrderController {

 

    @PostMapping(value = &quot;/&quot;)

    @PreAuthorize(&quot;hasRole(ROLE_ADMIN)&quot;)

    public void addOrder(@RequestBody Order order) {

        …

    }

}
</code></pre>
<p>从这个示例中可以看到，在“/orders/”这个 HTTP 端点上，我们添加了一个 @PreAuthorize 注解用来限制只有角色为“ROLE_ADMIN”的用户才能访问该端点。</p>
<p>其实，Spring Security 中用于授权的注解还有 @PostAuthorize，它与 @PreAuthorize 注解是一组，主要用于请求结束之后检查权限。因这种情况比较少见，这里我们不再继续展开，你可以翻阅相关资料学习。</p>
<h3>实现多维度访问授权方案</h3>
<p>我们知道 HTTP 端点是 Web 应用程序的一种资源，而每个 Web 应用程序对于自身资源的保护粒度因服务而异。对于一般的 HTTP 端点，用户可能通过认证就可以访问；对于一些重要的 HTTP 端点，用户在已认证的基础上还会有一些附加要求。</p>
<p>接下来，我们将讨论对资源进行保护的三种粒度级别。</p>
<ul>
<li><strong>用户级别：</strong> 该级别是最基本的资源保护级别，只要是认证用户就可能访问服务内的各种资源。</li>
<li><strong>用户+角色级别：</strong> 该级别在认证用户级别的基础上，还要求用户属于某一个或多个特定角色。</li>
<li><strong>用户+角色+操作级别：</strong> 该级别在认证用户+角色级别的基础上，对某些 HTTP 操作方法做了访问限制。</li>
</ul>
<p>基于配置方法和注解，我们可以轻松实现上述三种访问授权方案。</p>
<h4>使用用户级别保护服务访问</h4>
<p>这次，我们来到 SpringCSS 案例系统中的 customer-service，先来回顾一下 CustomerController 的内容，如下所示：</p>
<pre><code>@RestController

@RequestMapping(value=&quot;customers&quot;)

public class CustomerController {

    @Autowired

    private CustomerTicketService customerTicketService; 

    @PostMapping(value = &quot;/{accountId}/{orderNumber}&quot;)

    public CustomerTicket generateCustomerTicket( @PathVariable(&quot;accountId&quot;) Long accountId,

            @PathVariable(&quot;orderNumber&quot;) String orderNumber) {

        CustomerTicket customerTicket = customerTicketService.generateCustomerTicket(accountId, orderNumber);

        return customerTicket;

    }

    @GetMapping(value = &quot;/{id}&quot;)

    public CustomerTicket getCustomerTicketById(@PathVariable Long id) {

        CustomerTicket customerTicket = customerTicketService.getCustomerTicketById(id);

     return customerTicket;

    }

    @GetMapping(value = &quot;/{pageIndex}/{pageSize}&quot;)

    public List&lt;CustomerTicket&gt; getCustomerTicketList( @PathVariable(&quot;pageIndex&quot;) int pageIndex, @PathVariable(&quot;pageSize&quot;) int pageSize) {

        List&lt;CustomerTicket&gt; customerTickets = customerTicketService.getCustomerTickets(pageIndex, pageSize);

        return customerTickets;

    }

 

	@DeleteMapping(value = &quot;/{id}&quot;)

    public void deleteCustomerTicket( @PathVariable(&quot;id&quot;) Long id) {

        customerTicketService.deleteCustomerTicket(id);

    }

}
</code></pre>
<p>因为 CustomerController 是 SpringCSS 案例中的核心入口，所以我们认为它的所有端点都应该受到保护。于是，在 customer-service 中，我们创建了一个 SpringCssSecurityConfig 类继承 WebSecurityConfigurerAdapter，如下代码所示：</p>
<pre><code>@Configuration

public class SpringCssSecurityConfig extends WebSecurityConfigurerAdapter {

 

    @Override

    public void configure(HttpSecurity http) throws Exception {

 

        http.authorizeRequests()

            .anyRequest()

            .authenticated();

    }

}
</code></pre>
<p>位于 configure() 方法中的 .anyRequest().authenticated() 语句指定了访问 customer-service 下的所有端点的任何请求都需要进行验证。因此，当我们使用普通的 HTTP 请求访问 CustomerController 中的任何 URL（例如<a href="http://localhost:8083/customers/1">http://localhost:8083/customers/1</a>），将会得到如下图代码所示的错误信息，该错误信息明确指出资源的访问需要进行认证。</p>
<pre><code>{

    &quot;error&quot;: &quot;access_denied&quot;,

    &quot;error_description&quot;: &quot;Full authentication is required to access to this resource&quot;

}
</code></pre>
<p>记得 18 讲中覆写 WebSecurityConfigurerAdapter 的 config(AuthenticationManagerBuilder auth) 方法时提供了一个用户名“springcss_user”，现在我们就用这个用户名来添加用户认证信息并再次访问该端点。显然，因为此时我们传入的是有效的用户信息，所以可以满足认证要求。</p>
<h4>使用用户+角色级别保护服务访问</h4>
<p>对于某些安全性要求比较高的 HTTP 端点，我们通常需要限定访问的角色。</p>
<p>例如，customer-service 服务中涉及客户工单管理等核心业务，我们认为不应该给所有的认证用户开放资源访问入口，而应该限定只有角色为“ADMIN”的管理员才开放。这时，我们就可以使用认证用户+角色保护服务的访问控制机制，具体的示例代码如下所示：</p>
<pre><code>@Configuration

public class SpringCssSecurityConfig extends WebSecurityConfigurerAdapter {

 

    @Override

    public void configure(HttpSecurity http) throws Exception {

 

        http.authorizeRequests()

            .antMatchers(&quot;/customers/**&quot;)

            .hasRole(&quot;ADMIN&quot;)

            .anyRequest()

            .authenticated();

    }

}
</code></pre>
<p>在上述代码中可以看到，我们使用了 HttpSecurity 类中的 antMatchers(&quot;/customer/<strong>&quot;) 和 hasRole(&quot;ADMIN&quot;) 方法为访问&quot;/customers/</strong>&quot;的请求限定了角色，只有&quot;ADMIN&quot;角色的认证用户才能访问以&quot;/customers/&quot;为根地址的所有 URL。</p>
<p>如果我们使用了认证用户+角色的方式保护服务访问，使用角色为“USER”的认证用户“springcss_user”访问 customer-service 时就会出现如下所示的“access_denied”错误信息：</p>
<pre><code>{

    &quot;error&quot;: &quot;access_denied&quot;,

    &quot;error_description&quot;: &quot;Access is denied&quot;

}
</code></pre>
<p>而我们使用具有“ADMIN”角色的“springcss_admin”用户访问 customer-service 时，将会得到正常的返回信息，关于这点你可以自己做一些尝试。</p>
<h4>使用用户+角色+操作级别保护服务访问</h4>
<p>最后一种保护服务访问的策略粒度划分最细，在认证用户+角色的基础上，我们需要再对具体的 HTTP 操作进行限制。</p>
<p>在 customer-service 中，我们认为所有对客服工单的删除操作都很危险，因此可以使用 http.antMatchers(HttpMethod.DELETE, &quot;/customers/**&quot;) 方法对删除操作进行保护，示例代码如下：</p>
<pre><code>@Configuration

public class SpringCssSecurityConfig extends WebSecurityConfigurerAdapter {

 

    @Override

    public void configure(HttpSecurity http) throws Exception{

        http.authorizeRequests()

                .antMatchers(HttpMethod.DELETE, &quot;/customers/**&quot;)

                .hasRole(&quot;ADMIN&quot;)

                .anyRequest()

                .authenticated();

    }

}
</code></pre>
<p>上述代码的效果在于对“/customers”端点执行删除操作时，我们需要使用具有“ADMIN”角色的“springcss_admin”用户，执行其他操作时不需要。因为如果我们使用“springcss_user”账户执行删除操作，还是会出现“access_denied”错误信息。</p>
<h3>小结与预告</h3>
<p>通过 19 讲的学习，我们明确了 Web 应用程序中访问授权控制的三种粒度，并基于 SpringCSS 案例给出了三种粒度下的控制实现方式。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="18&#32;&#32;用户认证：如何基于&#32;Spring&#32;Security&#32;构建用户认证体系？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="20&#32;&#32;服务监控：如何使用&#32;Actuator&#32;组件实现系统监控？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434d5098ae70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
