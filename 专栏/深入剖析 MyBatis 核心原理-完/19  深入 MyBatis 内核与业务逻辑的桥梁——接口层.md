<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>19  深入 MyBatis 内核与业务逻辑的桥梁——接口层.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;领略&#32;MyBatis&#32;设计思维，突破持久化技术瓶颈.md">00 开篇词  领略 MyBatis 设计思维，突破持久化技术瓶颈.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;常见持久层框架赏析，到底是什么让你选择&#32;MyBatis？.md">01  常见持久层框架赏析，到底是什么让你选择 MyBatis？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;订单系统持久层示例分析，20&#32;分钟带你快速上手&#32;MyBatis.md">02  订单系统持久层示例分析，20 分钟带你快速上手 MyBatis.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;MyBatis&#32;源码环境搭建及整体架构解析.md">03  MyBatis 源码环境搭建及整体架构解析.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;MyBatis&#32;反射工具箱：带你领略不一样的反射设计思路.md">04  MyBatis 反射工具箱：带你领略不一样的反射设计思路.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;数据库类型体系与&#32;Java&#32;类型体系之间的“爱恨情仇”.md">05  数据库类型体系与 Java 类型体系之间的“爱恨情仇”.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;日志框架千千万，MyBatis&#32;都能兼容的秘密是什么？.md">06  日志框架千千万，MyBatis 都能兼容的秘密是什么？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;深入数据源和事务，把握持久化框架的两个关键命脉.md">07  深入数据源和事务，把握持久化框架的两个关键命脉.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;Mapper&#32;文件与&#32;Java&#32;接口的优雅映射之道.md">08  Mapper 文件与 Java 接口的优雅映射之道.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;基于&#32;MyBatis&#32;缓存分析装饰器模式的最佳实践.md">09  基于 MyBatis 缓存分析装饰器模式的最佳实践.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;鸟瞰&#32;MyBatis&#32;初始化，把握&#32;MyBatis&#32;启动流程脉络（上）.md">10  鸟瞰 MyBatis 初始化，把握 MyBatis 启动流程脉络（上）.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;鸟瞰&#32;MyBatis&#32;初始化，把握&#32;MyBatis&#32;启动流程脉络（下）.md">11  鸟瞰 MyBatis 初始化，把握 MyBatis 启动流程脉络（下）.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;深入分析动态&#32;SQL&#32;语句解析全流程（上）.md">12  深入分析动态 SQL 语句解析全流程（上）.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;深入分析动态&#32;SQL&#32;语句解析全流程（下）.md">13  深入分析动态 SQL 语句解析全流程（下）.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;探究&#32;MyBatis&#32;结果集映射机制背后的秘密（上）.md">14  探究 MyBatis 结果集映射机制背后的秘密（上）.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;探究&#32;MyBatis&#32;结果集映射机制背后的秘密（下）.md">15  探究 MyBatis 结果集映射机制背后的秘密（下）.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;StatementHandler：参数绑定、SQL&#32;执行和结果映射的奠基者.md">16  StatementHandler：参数绑定、SQL 执行和结果映射的奠基者.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;Executor&#32;才是执行&#32;SQL&#32;语句的幕后推手（上）.md">17  Executor 才是执行 SQL 语句的幕后推手（上）.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;Executor&#32;才是执行&#32;SQL&#32;语句的幕后推手（下）.md">18  Executor 才是执行 SQL 语句的幕后推手（下）.md</a>

                </li>
                <li>

                    <a class="current-tab" href="19&#32;&#32;深入&#32;MyBatis&#32;内核与业务逻辑的桥梁——接口层.md">19  深入 MyBatis 内核与业务逻辑的桥梁——接口层.md</a>
                    

                </li>
                <li>

                    
                    <a href="20&#32;&#32;插件体系让&#32;MyBatis&#32;世界更加精彩.md">20  插件体系让 MyBatis 世界更加精彩.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;深挖&#32;MyBatis&#32;与&#32;Spring&#32;集成底层原理.md">21  深挖 MyBatis 与 Spring 集成底层原理.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;基于&#32;MyBatis&#32;的衍生框架一览.md">22  基于 MyBatis 的衍生框架一览.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;结束语&#32;&#32;会使用只能默默“搬砖”，懂原理才能快速晋升.md">23 结束语  会使用只能默默“搬砖”，懂原理才能快速晋升.md</a>

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
                        <div><h1>19  深入 MyBatis 内核与业务逻辑的桥梁——接口层</h1>
<p>在前面的课时中，我们已经详细介绍了 MyBatis 的内核，其中涉及了 MyBatis 的初始化、SQL 参数的绑定、SQL 语句的执行、各类结果集的映射等，MyBatis 为了简化业务代码调用内核功能的成本，就为我们封装了一个接口层。</p>
<p>这一讲我们就来重点看一下 MyBatis 接口层的实现以及其中涉及的设计模式。</p>
<h3>策略模式</h3>
<p>在 MyBatis 接口层中用到了经典设计模式中的策略模式，所以这里我们就先来介绍一下策略模式相关的知识点。</p>
<p>我们在编写业务逻辑的时候，可能有很多方式都可以实现某个具体的功能。例如，按照购买次数对一个用户购买的全部商品进行排序，从而粗略地得知该用户复购率最高的商品，我们可以使用多种排序算法来实现这个功能，例如，归并排序、插入排序、选择排序等。在不同的场景中，我们需要根据不同的输入条件、数据量以及运行时环境，选择不同的排序算法来完成这一个功能。很多同学可能在实现这个逻辑的时候，会用 if...else... 的硬编码方式来选择不同的算法，但这显然是不符合“开放-封闭”原则的，当需要添加新的算法时，只能修改这个 if...else...代码块，添加新的分支，这就破坏了代码原有的稳定性。</p>
<p>在策略模式中，我们会<strong>将每个算法单独封装成不同的算法实现类</strong>（这些算法实现类都实现了相同的接口），每个算法实现类就可以被认为是一种策略实现，我们只需选择不同的策略实现来解决业务问题即可，这样每种算法相对独立，算法内的变化边界也就明确了，新增或减少算法实现也不会影响其他算法。</p>
<p>如下是策略模式的核心类图，其中 StrategyUser 是算法的调用方，维护了一个 Strategy 对象的引用，用来选择具体的算法实现。</p>
<p><img src="assets/CioPOWBdmRKAZosJAAEAw6jnBB8920.png" alt="图片2.png" /></p>
<p>策略模式的核心类图</p>
<h3>SqlSession</h3>
<p><strong>SqlSession是MyBatis对外提供的一个 API 接口，整个MyBatis 接口层也是围绕 SqlSession接口展开的</strong>，SqlSession 接口中定义了下面几类方法。</p>
<ul>
<li>select*() 方法：用来执行查询操作的方法，SqlSession 会将结果集映射成不同类型的结果对象，例如，selectOne() 方法返回单个 Java 对象，selectList()、selectMap() 方法返回集合对象。</li>
<li>insert()、update()、delete() 方法：用来执行 DML 语句。</li>
<li>commit()、rollback() 方法：用来控制事务。</li>
<li>getMapper()、getConnection()、getConfiguration() 方法：分别用来获取接口对应的 Mapper 对象、底层的数据库连接和全局的 Configuration 配置对象。</li>
</ul>
<p>如下图所示，MyBatis 提供了两个 SqlSession接口的实现类，同时提供了SqlSessionFactory 工厂类来创建 SqlSession 对象。</p>
<p><img src="assets/CioPOWBdmQiAIatQAAFZND8WjFQ155.png" alt="图片1.png" /></p>
<p>SqlSessionFactory 接口与 SqlSession 接口的实现类</p>
<p>默认情况下，<strong>我们在使用 MyBatis 的时候用的都是 DefaultSqlSession 这个默认的 SqlSession 实现</strong>。DefaultSqlSession 中维护了一个 Executor 对象，通过它来完成数据库操作以及事务管理。DefaultSqlSession 在选择使用哪种 Executor 实现的时候，使用到了策略模式：DefaultSqlSession 扮演了策略模式中的 StrategyUser 角色，Executor 接口扮演的是 Strategy 角色，Executor 接口的不同实现则对应 StrategyImpl 的角色。</p>
<p>另外，DefaultSqlSession 还维护了一个 dirty 字段来标识缓存中是否有脏数据，它在执行 update() 方法修改数据时会被设置为 true，并在后续参与事务控制，决定当前事务是否需要提交或回滚。</p>
<p>下面接着来看 DefaultSqlSession 对 SqlSession 接口的实现。DefaultSqlSession 为每一类数据操作方法提供了多个重载，尤其是 select*() 操作，而且这些 select*() 方法的重载之间有相互依赖的关系，如下图所示：</p>
<p><img src="assets/Cgp9HWBYb-iAKkKeAADz5INxXLw311.png" alt="Drawing 2.png" /></p>
<p>select() 方法之间的调用关系</p>
<p>通过上图我们可以清晰地看到，所有 select*() 方法最终都是通过调用 Executor.query() 方法执行 select 语句、完成数据查询操作的，之所以有不同的 select*() 重载，主要是对结果对象的需求不同。例如，我们使用 selectList() 重载时，希望返回的结果对象是一个 List集合；使用 selectMap() 重载时，希望查询到的结果集被转换成 Map 类型集合返回；至于select() 重载，则会由 ResultHandler 来处理结果对象。</p>
<p>DefaultSqlSession 中的 insert()、update()、delete() 等修改数据的方法以及 commit()、rollback() 等事务管理的方法，同样也有多个重载，它们最终也是委托到Executor 中的同名方法，完成数据修改操作以及事务管理操作的。</p>
<p>在事务管理的相关方法中，DefaultSqlSession 会根据 dirty 字段以及 autoCommit 字段（是否自动提交事务）、用户传入的 force参数（是否强制提交事务）共同决定是否提交/回滚事务，这部分逻辑位于 isCommitOrRollbackRequired() 方法中，具体实现如下：</p>
<pre><code>private boolean isCommitOrRollbackRequired(boolean force) {

    return (!autoCommit &amp;&amp; dirty) || force;

}
</code></pre>
<h3>DefaultSqlSessionFactory</h3>
<p><strong>DefaultSqlSessionFactory 是MyBatis中用来创建DefaultSqlSession 的具体工厂实现</strong>。通过 DefaultSqlSessionFactory 工厂类，我们可以有两种方式拿到 DefaultSqlSession对象。</p>
<p>第一种方式是通过数据源获取数据库连接，然后在其基础上创建 DefaultSqlSession 对象，其核心实现位于 openSessionFromDataSource() 方法，具体实现如下：</p>
<pre><code>// 获取Environment对象

final Environment environment = configuration.getEnvironment();

// 获取TransactionFactory对象

final TransactionFactory transactionFactory = getTransactionFactoryFromEnvironment(environment);

// 从数据源中创建Transaction

tx = transactionFactory.newTransaction(environment.getDataSource(), level, autoCommit);

// 根据配置创建Executor对象

final Executor executor = configuration.newExecutor(tx, execType);

// 在Executor的基础上创建DefaultSqlSession对象

return new DefaultSqlSession(configuration, executor, autoCommit);
</code></pre>
<p>第二种方式是上层调用方直接提供数据库连接，并在该数据库连接之上创建 DefaultSqlSession 对象，这种创建方式的核心逻辑位于 openSessionFromConnection() 方法中，核心实现如下：</p>
<pre><code>boolean autoCommit;

try {

    // 获取事务提交方式

    autoCommit = connection.getAutoCommit();

} catch (SQLException e) {

    autoCommit = true;

}

// 获取Environment对象、TransactionFactory

final Environment environment = configuration.getEnvironment();

final TransactionFactory transactionFactory = getTransactionFactoryFromEnvironment(environment);

// 通过Connection对象创建Transaction

final Transaction tx = transactionFactory.newTransaction(connection);

// 创建Executor对象

final Executor executor = configuration.newExecutor(tx, execType);

// 创建DefaultSqlSession对象

return new DefaultSqlSession(configuration, executor, autoCommit);
</code></pre>
<h3>SqlSessionManager</h3>
<p>通过前面的 SqlSession 继承关系图我们可以看到，SqlSessionManager 同时实现了 SqlSession 和 SqlSessionFactory 两个接口，也就是说，它<strong>同时具备操作数据库的能力和创建SqlSession的能力</strong>。</p>
<p>首先来看 SqlSessionManager <strong>创建SqlSession的实现</strong>。它与 DefaultSqlSessionFactory 的主要区别是：DefaultSqlSessionFactory 在一个线程多次获取 SqlSession 的时候，都会创建不同的 SqlSession对象；SqlSessionManager 则有<strong>两种模式</strong>，一种模式与 DefaultSqlSessionFactory 相同，另一种模式是 SqlSessionManager 在内部维护了一个 ThreadLocal 类型的字段（localSqlSession）来记录与当前线程绑定的 SqlSession 对象，同一线程从 SqlSessionManager 中获取的 SqlSession 对象始终是同一个，这样就减少了创建 SqlSession 对象的开销。</p>
<p>无论哪种模式，SqlSessionManager 都可以看作是 SqlSessionFactory 的装饰器，我们可以在 SqlSessionManager 的构造方法中看到，其中会传入一个 SqlSessionFactory 对象。</p>
<p>如果使用第一种模式，我们可以直接调用 SqlSessionManager.openSession() 方法，其底层直接调用被装饰的 SqlSessionFactory 对象创建 SqlSession 对象并返回。如果使用第二种模式，则需要调用 startManagedSession() 方法为当前线程绑定 SqlSession 对象，这里的 SqlSession 对象也是由被装饰的SqlSessionFactory 创建的，该模式的核心实现位于 startManagedSession() 方法中，具体实现如下：</p>
<pre><code>public void startManagedSession() {

    // 调用底层被装饰的SqlSessionFactory创建SqlSession对象，并绑定到localSqlSession字段中

    localSqlSession.set(openSession());

}
</code></pre>
<p>与当前线程绑定完成之后，我们就可以<strong>通过SqlSessionManager实现的SqlSession接口方法进行数据库操作</strong>了，这些数据操作底层都是调用 sqlSessionProxy 这个 SqlSession 代理实现的。</p>
<p>SqlSessionManager 中的 sqlSessionProxy 字段指向了一个通过 JDK 动态代理创建的代理类，其中使用的 InvocationHandler 实现是 SqlSessionManager 的内部类 SqlSessionInterceptor。SqlSessionInterceptor 在成功拦截目标方法之后，会首先通过 localSqlSession 字段检查当前线程是否已经绑定了 SqlSession，如果绑定了，则直接使用绑定的 SqlSession；如果没有绑定，则通过 openSession() 方法创建新 SqlSession 完成数据库操作。具体实现如下：</p>
<pre><code>public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {

    // 尝试从localSqlSession变量中获取当前线程绑定的SqlSession对象

    final SqlSession sqlSession = SqlSessionManager.this.localSqlSession.get();

    if (sqlSession != null) {

        try {

            // 当前线程已经绑定了SqlSession，直接使用即可

            return method.invoke(sqlSession, args);

        } catch (Throwable t) {

            throw ExceptionUtil.unwrapThrowable(t);

        }

    } else {

        // 通过openSession()方法创建新SqlSession对象

        try (SqlSession autoSqlSession = openSession()) {

            try {

                // 通过新建的SqlSession对象完成数据库操作

                final Object result = method.invoke(autoSqlSession, args);

                autoSqlSession.commit();

                return result;

            } catch (Throwable t) {

                autoSqlSession.rollback();

                throw ExceptionUtil.unwrapThrowable(t);

            }

        }

    }

}
</code></pre>
<p>SqlSessionManager中的 select*()、insert()、update() 等数据操作都依赖于 sqlSessionProxy 代理对象，而 commit()、rollback()、close() 方法等事务相关的操作，都是直接通过 localSqlSession 字段判断当前线程使用哪个 SqlSession。这里以 commit() 方法简单说明一下：</p>
<pre><code>public void commit() {

  // 获取当前线程绑定的SqlSession对象

  final SqlSession sqlSession = localSqlSession.get();

  if (sqlSession == null) { // 如果当前未绑定SqlSession对象，则不能用SqlSessionManager来控制事务

      throw new SqlSessionException(&quot;Error:  Cannot commit.  No managed session is started.&quot;);

  }

  // 如果当前线程绑定了SqlSession，则可以通过SqlSessionManager来提交事务

  sqlSession.commit();

}
</code></pre>
<h3>总结</h3>
<p>这一讲我们重点介绍了 MyBatis 中接口层的核心实现。MyBatis 接口层是基于前面课时介绍的核心处理层和基础支撑层对使用方提供的 API 接口，也就是我们在生产中最直接、最常用的接口。</p>
<p>这里我们首先介绍了 MyBatis 接口层使用到的策略模式这一经典设计模式的知识点，然后讲解了 SqlSession 接口的核心定义以及它的默认实现—— DefaultSqlSession，接下来还分析了用于创建 DefaultSqlSession 对象的工厂类——DefaultSqlSessionFactory，最后阐述了同时实现了 SqlSession 接口和 SqlSessionFactory 接口的 SqlSessionManager 实现类的核心原理。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="18&#32;&#32;Executor&#32;才是执行&#32;SQL&#32;语句的幕后推手（下）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="20&#32;&#32;插件体系让&#32;MyBatis&#32;世界更加精彩.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4357495bc9645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E6%B7%B1%E5%85%A5%E5%89%96%E6%9E%90%20MyBatis%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
