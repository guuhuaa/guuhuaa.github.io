<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>17  安全架构：如何理解 Spring 安全体系的整体架构？.md</title>
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

                    <a class="current-tab" href="17&#32;&#32;安全架构：如何理解&#32;Spring&#32;安全体系的整体架构？.md">17  安全架构：如何理解 Spring 安全体系的整体架构？.md</a>
                    

                </li>
                <li>

                    
                    <a href="18&#32;&#32;用户认证：如何基于&#32;Spring&#32;Security&#32;构建用户认证体系？.md">18  用户认证：如何基于 Spring Security 构建用户认证体系？.md</a>

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
                        <div><h1>17  安全架构：如何理解 Spring 安全体系的整体架构？</h1>
<p>在设计 Web 应用程序时，一方面，因为开发人员缺乏对 Web 安全访问机制的认识，所以系统安全性是一个重要但又容易被忽略的话题。另一方面，因为系统涉及的技术体系非常复杂，所以系统安全性又是一个非常综合的话题。因此，这一讲我们将讨论一个全新的话题—— Spring 中与安全性相关的需求和实现方案。</p>
<p>在 Spring 家族中，Spring Security 专门为开发人员提供了一个安全性开发框架，下面我们一起来看下Spring 中安全体系的整体架构。</p>
<h3>Web 应用程序的安全性需求</h3>
<p>在软件系统中，我们把需要访问的内容定义为一种资源（Resource），而安全性设计的核心目标是对这些资源进行保护，以此确保外部请求对它们的访问安全受控。</p>
<p>在一个 Web 应用程序中，我们把对外暴露的 RESTful 端点理解为资源，关于如何对 HTTP 端点这些资源进行安全性访问，业界存在一些常见的技术体系。</p>
<p>在讲解这些技术体系之前，我们先来看看安全领域中非常常见但又容易混淆的两个概念：<strong>认证（Authentication）和授权（Authorization）。</strong></p>
<p><strong>所谓认证</strong>，即首先需要明确“你是谁”这个问题，也就是说系统能针对每次访问请求判断出访问者是否具有合法的身份标识。</p>
<p>一旦明确了 “你是谁”，我们就能判断出“你能做什么”，这个步骤就是<strong>授权</strong>。一般来说，通用的授权模型都是基于权限管理体系，即对资源、权限、角色和用户的进行组合处理的一种方案。</p>
<p>当我们把认证与授权结合起来后，即先判断资源访问者的有效身份，然后确定其对这个资源进行访问的合法权限，整个过程就形成了对系统进行安全性管理的一种常见解决方案，如下图所示：</p>
<p><img src="assets/Cip5yF_9eRGAaOFAAACdJ5DTEOU093.png" alt="Drawing 1.png" /></p>
<p>基于认证和授权机制的资源访问安全性示意图</p>
<p>上图就是一种通用方案，而在不同的应用场景及技术体系下，系统可以衍生出很多具体的实现策略，比如 Web 应用系统中的认证和授权模型虽然与上图类似，但是在具体设计和实现过程中有其特殊性。</p>
<p>在 Web 应用体系中，因为认证这部分的需求相对比较明确，所以我们需要构建一套完整的存储体系来保存和维护用户信息，并且确保这些用户信息在处理请求的过程中能够得到合理利用。</p>
<p>而授权的情况相对来说复杂些，比如对某个特定的 Web 应用程序而言，我们面临的第一个问题是如何判断一个 HTTP 请求具备访问自己的权限。解决完这个第一个问题后，就算这个请求具备访问该应用程序的权限，并不意味着它能够访问其所具有的所有 HTTP 端点，比如业务上的某些核心功能还是需要具备较高的权限才能访问，这就涉及我们需要解决的第二个问题——如何对访问的权限进行精细化管理？如下图所示：</p>
<p><img src="assets/Ciqc1F_9eRqANunuAAB5IYtX-6s596.png" alt="Drawing 3.png" /></p>
<p>Web 应用程序访问授权效果示意图</p>
<p>在上图中，假设该请求具备对 Web 应用程序的访问权限，但不具备访问应用程序中端点 1 的权限，如果想实现这种效果，一般我们的做法是引入角色体系：首先对不同的用户设置不同等级的角色（即角色等级不同对应的访问权限也不同），再把每个请求绑定到某个角色（即该请求具备了访问权限）。</p>
<p>接下来我们把认证和授权进行结合，梳理出了 Web 应用程序访问场景下的安全性实现方案，如下图所示：</p>
<p><img src="assets/CgqCHl_9eSOANBbmAACWXd-B08c635.png" alt="Drawing 5.png" /></p>
<p>认证和授权整合示意图</p>
<p>从上图我们可以看到，用户首先通过请求传递用户凭证完成用户认证，然后根据该用户信息中所具备的角色信息获取访问权限，最终完成对 HTTP 端点的访问授权。</p>
<p>对一个 Web 应用程序进行安全性设计时，我们首先需要考虑认证和授权，因为它们是核心考虑点。在技术实现场景中，只要涉及用户认证，势必会涉及用户密码等敏感信息的加密。针对用户密码的场景，我们主要使用单向散列加密算法对敏感信息进行加密。</p>
<p>关于单向散列加密算法，它常用于生成消息摘要（Message Digest），主要特点为单向不可逆和密文长度固定，同时具备“碰撞”少的优点，即明文的微小差异会导致生成的密文完全不同。其中，常见的单向散列加密实现算法为 MD5（Message Digest 5）和 SHA（Secure Hash Algorithm）。而在 JDK 自带的 MessageDigest 类中，因为它已经包含了这些算法的默认实现，所以我们直接调用方法即可。</p>
<p>在日常开发过程中，对于密码进行加密的典型操作时序图如下所示：</p>
<p><img src="assets/CgpVE1_24-6ACO9pAABbleIQe14786.png" alt="Drawing 3.png" /></p>
<p>单向散列加密与加盐机制</p>
<p>上图中，我们引入了加盐（Salt）机制，进一步提升了加密数据的安全性。所谓加盐就是在初始化明文数据时，系统自动往明文中添加一些附加数据，然后再进行散列。</p>
<p>目前，单向散列加密及加盐思想已被广泛用于系统登录过程中的密码生成和校验过程中，比如接下来我们将要引入的 Spring Security 框架。</p>
<h3>Spring Security 架构</h3>
<p>Spring Security 是 Spring 家族中历史比较悠久的一个框架，在 Spring Boot 出现之前，Spring Security 已经发展了很多年，尽管 Spring Security 的功能非常丰富，相比 Apache Shiro 这种轻量级的安全框架，它的优势就不那么明显了，加之应用程序中集成和配置 Spring Security 框架的过程比较复杂，因此它的发展过程并不是那么顺利。</p>
<p>而正是随着 Spring Boot 的兴起，带动了 Spring Security 的发展。它专门针对 Spring Security 提供了一套完整的自动配置方案，使得开发人员可以零配置使用 Spring Security。</p>
<p>这一讲我们先不对如何使用 Spring Security 框架展开说明，而是先从高层次梳理该框架对前面提到的各项安全性需求提供的架构设计。</p>
<h4>Spring Security 中的过滤器链</h4>
<p>与业务中大多数处理 Web 请求的框架对比后，我们发现 Spring Security 中采用的是管道-过滤器（Pipe-Filter）架构模式，如下图所示：</p>
<p><img src="assets/CgqCHl_9eTCACoPnAACF6H2W2KI357.png" alt="Drawing 8.png" /></p>
<p>管道-过滤器架构模式示意图</p>
<p>在上图中我们可以看到，处理业务逻辑的组件称为过滤器，而处理结果的相邻过滤器之间的连接件称为管道，它们构成了一组过滤器链，即 Spring Security 的核心。</p>
<p>项目一旦启动，过滤器链将会实现自动配置，如下图所示：</p>
<p><img src="assets/Ciqc1F_9eTmAM6OYAAD0pSOc1Xg188.png" alt="Drawing 10.png" /></p>
<p>Spring Security 中的过滤器链</p>
<p>在上图中，我们看到了 BasicAuthenticationFilter、UsernamePasswordAuthenticationFilter 等几个常见的 Filter，这些类可以直接或间接实现 Servlet 类中的 Filter 接口，并完成某一项具体的认证机制。例如，上图中的 BasicAuthenticationFilter 用来认证用户的身份，而 UsernamePasswordAuthenticationFilter 用来检查输入的用户名和密码，并根据认证结果来判断是否将结果传递给下一个过滤器。</p>
<p>这里请注意，整个 Spring Security 过滤器链的末端是一个 FilterSecurityInterceptor，本质上它也是一个 Filter，但它与其他用于完成认证操作的 Filter 不同，因为它的核心功能是用来实现权限控制，即判定该请求是否能够访问目标 HTTP 端点。因为我们可以把 FilterSecurityInterceptor 对权限控制的粒度划分到方法级别，所以它能够满足前面提到的精细化访问控制。</p>
<p>通过上述分析，我们知道了在 Spring Security 中，认证和授权这两个安全性需求主要通过一系列的过滤器进行实现。</p>
<p>基于过滤器链，我们再来深入分析下 Spring Security 的核心类结构。</p>
<h4>Spring Security 中的核心类</h4>
<p>我们先以最基础的 UsernamePasswordAuthenticationFilter 为例，该类的定义及核心方法 attemptAuthentication 如下代码所示。</p>
<pre><code>public class UsernamePasswordAuthenticationFilter extends

        AbstractAuthenticationProcessingFilter {

 

    public Authentication attemptAuthentication(HttpServletRequest request,

            HttpServletResponse response) throws AuthenticationException {

        if (postOnly &amp;&amp; !request.getMethod().equals(&quot;POST&quot;)) {

            throw new AuthenticationServiceException(

                    &quot;Authentication method not supported: &quot; + request.getMethod());

        }

 

        String username = obtainUsername(request);

        String password = obtainPassword(request);

 

        if (username == null) {

            username = &quot;&quot;;

        }

 

        if (password == null) {

            password = &quot;&quot;;

        }

 

        username = username.trim();

 

        UsernamePasswordAuthenticationToken authRequest = new UsernamePasswordAuthenticationToken(

                username, password);

 

        // Allow subclasses to set the &quot;details&quot; property

        setDetails(request, authRequest);

 

        return this.getAuthenticationManager().authenticate(authRequest);

    }

    …

}
</code></pre>
<p>围绕上述方法，通过翻阅 Spring Security 源代码，我们引出了该框架中一系列核心类，并梳理了它们之间的交互结构，如下图所示：</p>
<p><img src="assets/Cip5yF_9edmAN_FuAAD0M-rwB1I928.png" alt="Lark20210112-182830.png" /></p>
<p>Spring Security 核心类图</p>
<p>上图中的很多类，通过名称我们就能明白它的含义和作用。</p>
<p>以位于左下角的 SecurityContextHolder 为例，它是一个典型的 Holder 类，存储了应用的安全上下文对象 SecurityContext，包含系统请求中最近使用的认证信息。这里我们大胆猜想它的内部肯定使用了 ThreadLocal 来确保线程访问的安全性。</p>
<p>而正如 UsernamePasswordAuthenticationFilter 中的代码所示，一个 HTTP 请求到达系统后，将通过一系列的 Filter 完成用户认证，然后具体的工作交由 AuthenticationManager 完成，AuthenticationManager 成功验证后会返回填充好的 Authentication 实例。</p>
<p>AuthenticationManager 是一个接口，在其实现 ProviderManager 类时会进一步依赖 AuthenticationProvider 接口完成具体的认证工作。</p>
<p>而在 Spring Security 中存在一大批 AuthenticationProvider 接口的实现类，分别完成各种认证操作。在执行具体的认证工作时，Spring Security 势必会使用用户详细信息，上图位于右边的 UserDetailsService 服务就是用来对用户详细信息实现管理。</p>
<p>关于上图中的很多其他核心类，我们将在后续的 18 讲《用户认证：如何基于Spring Security 构建用户认证体系？》中持续深入展开。</p>
<h3>小结与预告</h3>
<p>这一讲我们开始探讨 Web 应用程序的安全性，在这个领域中，因为认证和授权仍然是最基本的安全性控制手段，因此我们系统分析了认证和授权的解决方案，并引入了 Spring 家族中的 Spring Security 框架实现这一解决方案，同时对 Spring Security 的基本架构做了分析。</p>
<p>介绍完认证和授权的基本概念之后，18 讲我们将基于 SpringCSS 案例系统详细介绍它们的实现过程，首先我们需要关注如何使用 Spring Security 框架完成对用户认证过程的管理。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="16&#32;&#32;消息驱动：如何使用&#32;RabbitTemplate&#32;集成&#32;RabbitMQ？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="18&#32;&#32;用户认证：如何基于&#32;Spring&#32;Security&#32;构建用户认证体系？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434d3e5d1c70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
