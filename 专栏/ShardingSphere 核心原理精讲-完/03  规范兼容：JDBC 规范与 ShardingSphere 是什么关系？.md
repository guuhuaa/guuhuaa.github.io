<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>03  规范兼容：JDBC 规范与 ShardingSphere 是什么关系？.md</title>
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

                    
                    <a href="00&#32;如何正确学习一款分库分表开源框架？.md">00 如何正确学习一款分库分表开源框架？.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;从理论到实践：如何让分库分表真正落地？.md">01  从理论到实践：如何让分库分表真正落地？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;顶级项目：ShardingSphere&#32;是一款什么样的&#32;Apache&#32;开源软件？.md">02  顶级项目：ShardingSphere 是一款什么样的 Apache 开源软件？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="03&#32;&#32;规范兼容：JDBC&#32;规范与&#32;ShardingSphere&#32;是什么关系？.md">03  规范兼容：JDBC 规范与 ShardingSphere 是什么关系？.md</a>
                    

                </li>
                <li>

                    
                    <a href="04&#32;&#32;应用集成：在业务系统中使用&#32;ShardingSphere&#32;的方式有哪些？.md">04  应用集成：在业务系统中使用 ShardingSphere 的方式有哪些？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;配置驱动：ShardingSphere&#32;中的配置体系是如何设计的？.md">05  配置驱动：ShardingSphere 中的配置体系是如何设计的？.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ShardingSphere%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86%E7%B2%BE%E8%AE%B2-%E5%AE%8C/06%20%20%E6%95%B0%E6%8D%AE%E5%88%86%E7%89%87%EF%BC%9A%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%88%86%E5%BA%93%E3%80%81%E5%88%86%E8%A1%A8%E3%80%81%E5%88%86%E5%BA%93+%E5%88%86%E8%A1%A8%E4%BB%A5%E5%8F%8A%E5%BC%BA%E5%88%B6%E8%B7%AF%E7%94%B1%EF%BC%9F%EF%BC%88%E4%B8%8A%EF%BC%89.md">06  数据分片：如何实现分库、分表、分库+分表以及强制路由？（上）.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ShardingSphere%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86%E7%B2%BE%E8%AE%B2-%E5%AE%8C/07%20%20%E6%95%B0%E6%8D%AE%E5%88%86%E7%89%87%EF%BC%9A%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%88%86%E5%BA%93%E3%80%81%E5%88%86%E8%A1%A8%E3%80%81%E5%88%86%E5%BA%93+%E5%88%86%E8%A1%A8%E4%BB%A5%E5%8F%8A%E5%BC%BA%E5%88%B6%E8%B7%AF%E7%94%B1%EF%BC%9F%EF%BC%88%E4%B8%8B%EF%BC%89.md">07  数据分片：如何实现分库、分表、分库+分表以及强制路由？（下）.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ShardingSphere%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86%E7%B2%BE%E8%AE%B2-%E5%AE%8C/08%20%20%E8%AF%BB%E5%86%99%E5%88%86%E7%A6%BB%EF%BC%9A%E5%A6%82%E4%BD%95%E9%9B%86%E6%88%90%E5%88%86%E5%BA%93%E5%88%86%E8%A1%A8+%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%BB%E4%BB%8E%E6%9E%B6%E6%9E%84%EF%BC%9F.md">08  读写分离：如何集成分库分表+数据库主从架构？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;分布式事务：如何使用强一致性事务与柔性事务？.md">09  分布式事务：如何使用强一致性事务与柔性事务？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;数据脱敏：如何确保敏感数据的安全访问？.md">10  数据脱敏：如何确保敏感数据的安全访问？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;编排治理：如何实现分布式环境下的动态配置管理？.md">11  编排治理：如何实现分布式环境下的动态配置管理？.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;从应用到原理：如何高效阅读&#32;ShardingSphere&#32;源码？.md">12  从应用到原理：如何高效阅读 ShardingSphere 源码？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;微内核架构：ShardingSphere&#32;如何实现系统的扩展性？.md">13  微内核架构：ShardingSphere 如何实现系统的扩展性？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;分布式主键：ShardingSphere&#32;中有哪些分布式主键实现方式？.md">14  分布式主键：ShardingSphere 中有哪些分布式主键实现方式？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;解析引擎：SQL&#32;解析流程应该包括哪些核心阶段？（上）.md">15  解析引擎：SQL 解析流程应该包括哪些核心阶段？（上）.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;解析引擎：SQL&#32;解析流程应该包括哪些核心阶段？（下）.md">16  解析引擎：SQL 解析流程应该包括哪些核心阶段？（下）.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;路由引擎：如何理解分片路由核心类&#32;ShardingRouter&#32;的运作机制？.md">17  路由引擎：如何理解分片路由核心类 ShardingRouter 的运作机制？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;路由引擎：如何实现数据访问的分片路由和广播路由？.md">18  路由引擎：如何实现数据访问的分片路由和广播路由？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;路由引擎：如何在路由过程中集成多种路由策略和路由算法？.md">19  路由引擎：如何在路由过程中集成多种路由策略和路由算法？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;改写引擎：如何理解装饰器模式下的&#32;SQL&#32;改写实现机制？.md">20  改写引擎：如何理解装饰器模式下的 SQL 改写实现机制？.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;执行引擎：分片环境下&#32;SQL&#32;执行的整体流程应该如何进行抽象？.md">21  执行引擎：分片环境下 SQL 执行的整体流程应该如何进行抽象？.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;执行引擎：如何把握&#32;ShardingSphere&#32;中的&#32;Executor&#32;执行模型？（上）.md">22  执行引擎：如何把握 ShardingSphere 中的 Executor 执行模型？（上）.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;执行引擎：如何把握&#32;ShardingSphere&#32;中的&#32;Executor&#32;执行模型？（下）.md">23  执行引擎：如何把握 ShardingSphere 中的 Executor 执行模型？（下）.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;归并引擎：如何理解数据归并的类型以及简单归并策略的实现过程？.md">24  归并引擎：如何理解数据归并的类型以及简单归并策略的实现过程？.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;归并引擎：如何理解流式归并和内存归并在复杂归并场景下的应用方式？.md">25  归并引擎：如何理解流式归并和内存归并在复杂归并场景下的应用方式？.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;&#32;读写分离：普通主从架构和分片主从架构分别是如何实现的？.md">26  读写分离：普通主从架构和分片主从架构分别是如何实现的？.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;&#32;分布式事务：如何理解&#32;ShardingSphere&#32;中对分布式事务的抽象过程？.md">27  分布式事务：如何理解 ShardingSphere 中对分布式事务的抽象过程？.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;&#32;分布式事务：ShardingSphere&#32;中如何集成强一致性事务和柔性事务支持？（上）.md">28  分布式事务：ShardingSphere 中如何集成强一致性事务和柔性事务支持？（上）.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;&#32;分布式事务：ShardingSphere&#32;中如何集成强一致性事务和柔性事务支持？（下）.md">29  分布式事务：ShardingSphere 中如何集成强一致性事务和柔性事务支持？（下）.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;&#32;数据脱敏：如何基于改写引擎实现低侵入性数据脱敏方案？.md">30  数据脱敏：如何基于改写引擎实现低侵入性数据脱敏方案？.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;配置中心：如何基于配置中心实现配置信息的动态化管理？.md">31 配置中心：如何基于配置中心实现配置信息的动态化管理？.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;注册中心：如何基于注册中心实现数据库访问熔断机制？.md">32 注册中心：如何基于注册中心实现数据库访问熔断机制？.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;链路跟踪：如何基于&#32;Hook&#32;机制以及&#32;OpenTracing&#32;协议实现数据访问链路跟踪？.md">33 链路跟踪：如何基于 Hook 机制以及 OpenTracing 协议实现数据访问链路跟踪？.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ShardingSphere%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86%E7%B2%BE%E8%AE%B2-%E5%AE%8C/34%20%E7%B3%BB%E7%BB%9F%E9%9B%86%E6%88%90%EF%BC%9A%E5%A6%82%E4%BD%95%E5%AE%8C%E6%88%90%20ShardingSphere%20%E5%86%85%E6%A0%B8%E4%B8%8E%20Spring+SpringBoot%20%E7%9A%84%E6%97%A0%E7%BC%9D%E6%95%B4%E5%90%88%EF%BC%9F.md">34 系统集成：如何完成 ShardingSphere 内核与 Spring+SpringBoot 的无缝整合？.md</a>

                </li>
                <li>

                    
                    <a href="35&#32;结语：ShardingSphere&#32;总结及展望.md">35 结语：ShardingSphere 总结及展望.md</a>

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
                        <div><h1>03  规范兼容：JDBC 规范与 ShardingSphere 是什么关系？</h1>
<p>我们知道 ShardingSphere 是一种典型的客户端分片解决方案，而客户端分片的实现方式之一就是重写 JDBC 规范。在上一课时中，我们也介绍了，ShardingSphere 在设计上从一开始就完全兼容 JDBC 规范，ShardingSphere 对外暴露的一套分片操作接口与 JDBC 规范中所提供的接口完全一致。</p>
<p>讲到这里，你可能会觉得有点神奇，<strong>ShardingSphere 究竟是通过什么方式，实现了与 JDBC 规范完全兼容的 API 来提供分片功能呢？</strong></p>
<p>这个问题非常重要，值得我们专门花一个课时的内容来进行分析和讲解。可以说，<strong>理解 JDBC 规范以及 ShardingSphere 对 JDBC 规范的重写方式，是正确使用 ShardingSphere 实现数据分片的前提</strong>。今天，我们就深入讨论 JDBC 规范与 ShardingSphere 的这层关系，帮你从底层设计上解开其中的神奇之处。</p>
<h3>JDBC 规范简介</h3>
<p>ShardingSphere 提供了与 JDBC 规范完全兼容的实现过程，在对这一过程进行详细展开之前，先来回顾一下 JDBC 规范。<strong>JDBC（Java Database Connectivity）的设计初衷是提供一套用于各种数据库的统一标准</strong>，而不同的数据库厂家共同遵守这套标准，并提供各自的实现方案供应用程序调用。作为统一标准，JDBC 规范具有完整的架构体系，如下图所示：</p>
<p><img src="assets/CgqCHl7xtaiASay6AAB0vuO1kAA457.png" alt="Drawing 0.png" /></p>
<p>JDBC 架构中的 Driver Manager 负责加载各种不同的驱动程序（Driver），并根据不同的请求，向调用者返回相应的数据库连接（Connection）。而应用程序通过调用 JDBC API 来实现对数据库的操作。<strong>对于开发人员而言，JDBC API 是我们访问数据库的主要途径，也是 ShardingSphere 重写 JDBC 规范并添加分片功能的入口</strong>。如果我们使用 JDBC 开发一个访问数据库的处理流程，常见的代码风格如下所示：</p>
<pre><code>// 创建池化的数据源
PooledDataSource dataSource = new PooledDataSource ();
// 设置MySQL Driver
dataSource.setDriver (&quot;com.mysql.jdbc.Driver&quot;);
// 设置数据库URL、用户名和密码
dataSource.setUrl (&quot;jdbc:mysql://localhost:3306/test&quot;);
dataSource.setUsername (&quot;root&quot;);
dataSource.setPassword (&quot;root&quot;);
// 获取连接
Connection connection = dataSource.getConnection();
// 执行查询
PreparedStatement statement = connection.prepareStatement (&quot;select * from user&quot;);
// 获取查询结果应该处理
ResultSet resultSet = statement.executeQuery();
while (resultSet.next()) {
	…
}
// 关闭资源
statement.close();
resultSet.close();
connection.close();
</code></pre>
<p>这段代码中包含了 JDBC API 中的核心接口，使用这些核心接口是我们基于 JDBC 进行数据访问的基本方式，这里有必要对这些接口的作用和使用方法做一些展开。事实上，随着课程内容的不断演进，你会发现在 ShardingSphere 中，完成日常开发所使用的也就是这些接口。</p>
<h4>DataSource</h4>
<p>DataSource 在 JDBC 规范中代表的是一种数据源，核心作用是获取数据库连接对象 Connection。在 JDBC 规范中，实际可以直接通过 DriverManager 获取 Connection。我们知道获取 Connection 的过程需要建立与数据库之间的连接，而这个过程会产生较大的系统开销。</p>
<p>为了提高性能，通常会建立一个中间层，该中间层将 DriverManager 生成的 Connection 存放到连接池中，然后从池中获取 Connection，可以认为，DataSource 就是这样一个中间层。在日常开发过程中，我们通常都会基于 DataSource 来获取 Connection。而在 ShardingSphere 中，暴露给业务开发人员的同样是一个经过增强的 DataSource 对象。DataSource 接口的定义是这样的：</p>
<pre><code>public interface DataSource  extends CommonDataSource, Wrapper {
  Connection getConnection() throws SQLException; 
  Connection getConnection(String username, String password)
    throws SQLException;
}
</code></pre>
<p>可以看到，DataSource 接口提供了两个获取 Connection 的重载方法，并继承了 CommonDataSource 接口，该接口是 JDBC 中关于数据源定义的根接口。除了 DataSource 接口之外，它还有两个子接口：</p>
<p><img src="assets/CgqCHl7xtbuALDZqAABj4c2IofU664.png" alt="Drawing 1.png" /></p>
<p>其中，DataSource 是官方定义的获取 Connection 的基础接口，ConnectionPoolDataSource 是从连接池 ConnectionPool 中获取的 Connection 接口。而 XADataSource 则用来实现在分布式事务环境下获取 Connection，我们在讨论 ShardingSphere 的分布式事务时会接触到这个接口。</p>
<p><strong>请注意，DataSource 接口同时还继承了一个 Wrapper 接口</strong>。从接口的命名上看，可以判断该接口应该起到一种包装器的作用，事实上，由于很多数据库供应商提供了超越标准 JDBC API 的扩展功能，所以，Wrapper 接口可以把一个由第三方供应商提供的、非 JDBC 标准的接口包装成标准接口。以 DataSource 接口为例，如果我们想要实现自己的数据源 MyDataSource，就可以提供一个实现了 Wrapper 接口的 MyDataSourceWrapper 类来完成包装和适配：</p>
<p><img src="assets/CgqCHl7xtdOAZEGNAABnV-ZtNrk288.png" alt="Drawing 2.png" /></p>
<p>在 JDBC 规范中，除了 DataSource 之外，Connection、Statement、ResultSet 等核心对象也都继承了这个接口。显然，ShardingSphere 提供的就是非 JDBC 标准的接口，所以也应该会用到这个 Wrapper 接口，并提供了类似的实现方案。</p>
<h4>Connection</h4>
<p>DataSource 的目的是获取 Connection 对象，我们可以把 Connection 理解为一种<strong>会话（Session）机制</strong>。Connection 代表一个数据库连接，负责完成与数据库之间的通信。所有 SQL 的执行都是在某个特定 Connection 环境中进行的，同时它还提供了一组重载方法，分别用于创建 Statement 和 PreparedStatement。另一方面，Connection 也涉及事务相关的操作，为了实现分片操作，ShardingSphere 同样也实现了定制化的 Connection 类 ShardingConnection。</p>
<h4>Statement</h4>
<p>JDBC 规范中的 Statement 存在两种类型，一种是<strong>普通的 Statement</strong>，一种是<strong>支持预编译的 PreparedStatement</strong>。所谓预编译，是指数据库的编译器会对 SQL 语句提前编译，然后将预编译的结果缓存到数据库中，这样下次执行时就可以替换参数并直接使用编译过的语句，从而提高 SQL 的执行效率。当然，这种预编译也需要成本，所以在日常开发中，对数据库只执行一次性读写操作时，用 Statement 对象进行处理比较合适；而当涉及 SQL 语句的多次执行时，可以使用 PreparedStatement。</p>
<p>如果需要查询数据库中的数据，只需要调用 Statement 或 PreparedStatement 对象的 executeQuery 方法即可，该方法以 SQL 语句作为参数，执行完后返回一个 JDBC 的 ResultSet 对象。当然，Statement 或 PreparedStatement 中提供了一大批执行 SQL 更新和查询的重载方法。在 ShardingSphere 中，同样也提供了 ShardingStatement 和 ShardingPreparedStatement 这两个支持分片操作的 Statement 对象。</p>
<h4>ResultSet</h4>
<p>一旦通过 Statement 或 PreparedStatement 执行了 SQL 语句并获得了 ResultSet 对象后，那么就可以通过调用 Resulset 对象中的 next() 方法遍历整个结果集。如果 next() 方法返回为 true，就意味结果集中存在数据，则可以调用 ResultSet 对象的一系列 getXXX() 方法来取得对应的结果值。对于分库分表操作而言，因为涉及从多个数据库或数据表中获取目标数据，势必需要对获取的结果进行归并。因此，ShardingSphere 中也提供了分片环境下的 ShardingResultSet 对象。</p>
<p>作为总结，我们梳理了基于 JDBC 规范进行数据库访问的开发流程图，如下图所示：</p>
<p><img src="assets/Ciqc1F7xteqAQsj5AAB1bj_eu10085.png" alt="Drawing 3.png" /></p>
<p>ShardingSphere 提供了与 JDBC 规范完全兼容的 API。也就是说，开发人员可以基于这个开发流程和 JDBC 中的核心接口完成分片引擎、数据脱敏等操作，我们来看一下。</p>
<h3>基于适配器模式的 JDBC 重写实现方案</h3>
<p>在 ShardingSphere 中，实现与 JDBC 规范兼容性的基本策略就是采用了设计模式中的适配器模式（Adapter Pattern）。<strong>适配器模式通常被用作连接两个不兼容接口之间的桥梁，涉及为某一个接口加入独立的或不兼容的功能。</strong></p>
<p>作为一套适配 JDBC 规范的实现方案，ShardingSphere 需要对上面介绍的 JDBC API 中的 DataSource、Connection、Statement 及 ResultSet 等核心对象都完成重写。虽然这些对象承载着不同功能，但重写机制应该是共通的，否则就需要对不同对象都实现定制化开发，显然，这不符合我们的设计原则。为此，ShardingSphere 抽象并开发了一套基于适配器模式的实现方案，整体结构是这样的，如下图所示：</p>
<p><img src="assets/Ciqc1F7xtfeAIlV7AABhpWkSy7c199.png" alt="Drawing 4.png" /></p>
<p>首先，我们看到这里有一个 JdbcObject 接口，这个接口泛指 JDBC API 中的 DataSource、Connection、Statement 等核心接口。前面提到，这些接口都继承自包装器 Wrapper 接口。ShardingSphere 为这个 Wrapper 接口提供了一个实现类 WrapperAdapter，这点在图中得到了展示。在 ShardingSphere 代码工程 sharding-jdbc-core 的 org.apache.shardingsphere.shardingjdbc.jdbc.adapter 包中包含了所有与 Adapter 相关的实现类：</p>
<p><img src="assets/Ciqc1F7xtgWAb3PaAAAW8D9SY1w475.png" alt="Drawing 5.png" /></p>
<p>在 ShardingSphere 基于适配器模式的实现方案图的底部，有一个 ShardingJdbcObject 类的定义。这个类也是一种泛指，代表 ShardingSphere 中用于分片的 ShardingDataSource、ShardingConnection、ShardingStatement 等对象。</p>
<p>最后发现 ShardingJdbcObject 继承自一个 AbstractJdbcObjectAdapter，而 AbstractJdbcObjectAdapter 又继承自 AbstractUnsupportedOperationJdbcObject，这两个类都是抽象类，而且也都泛指一组类。两者的区别在于，AbstractJdbcObjectAdapter 只提供了针对 JdbcObject 接口的一部分实现方法，这些方法是我们完成分片操作所需要的。而对于那些我们不需要的方法实现，则全部交由 AbstractUnsupportedOperationJdbcObject 进行实现，这两个类的所有方法的合集，就是原有 JdbcObject 接口的所有方法定义。</p>
<p>这样，我们大致了解了 ShardingSphere 对 JDBC 规范中核心接口的重写机制。这个重写机制非常重要，在 ShardingSphere 中应用也很广泛，我们可以通过示例对这一机制做进一步理解。</p>
<h3>ShardingSphere 重写 JDBC 规范示例：ShardingConnection</h3>
<p>通过前面的介绍，我们知道 ShardingSphere 的分片引擎中提供了一系列 ShardingJdbcObject 来支持分片操作，包括 ShardingDataSource、ShardingConnection、ShardingStatement、ShardingPreparedStament 等。这里以最具代表性的 ShardingConnection 为例，来讲解它的实现过程。请注意，今天我们关注的还是重写机制，不会对 ShardingConnection 中的具体功能以及与其他类之间的交互过程做过多展开讲解。</p>
<h4>ShardingConnection 类层结构</h4>
<p>ShardingConnection 是对 JDBC 中 Connection 的适配和包装，所以它需要提供 Connection 接口中定义的方法，包括 createConnection、getMetaData、各种重载的 prepareStatement 和 createStatement 以及针对事务的 setAutoCommit、commit 和 rollback 方法等。ShardingConnection 对这些方法都进行了重写，如下图所示：</p>
<p><img src="assets/CgqCHl7xthSAHp4DAACJDJsvmyk879.png" alt="Drawing 6.png" />
ShardingConnection 中的方法列表图</p>
<p>ShardingConnection 类的一条类层结构支线就是适配器模式的具体应用，这部分内容的类层结构与前面介绍的重写机制的类层结构是完全一致的，如下图所示：</p>
<p><img src="assets/CgqCHl9MudqAOb9wAAEeGv0YTn807.jpeg" alt="111.jpeg" /></p>
<h4>AbstractConnectionAdapter</h4>
<p>我们首先来看看 AbstractConnectionAdapter 抽象类，ShardingConnection 直接继承了它。在 AbstractConnectionAdapter 中发现了一个 cachedConnections 属性，它是一个 Map 对象，该对象其实缓存了这个经过封装的 ShardingConnection 背后真实的 Connection 对象。如果我们对一个 AbstractConnectionAdapter 重复使用，那么这些 cachedConnections 也会一直被缓存，直到调用 close 方法。可以从 AbstractConnectionAdapter 的 getConnections 方法中理解具体的操作过程：</p>
<pre><code>public final List&lt;Connection&gt; getConnections(final ConnectionMode connectionMode, final String dataSourceName, final int connectionSize) throws SQLException {
        //获取DataSource
        DataSource dataSource = getDataSourceMap().get(dataSourceName);
        Preconditions.checkState(null != dataSource, &quot;Missing the data source name: '%s'&quot;, dataSourceName);
        Collection&lt;Connection&gt; connections;

        //根据数据源从cachedConnections中获取connections
        synchronized (cachedConnections) {
            connections = cachedConnections.get(dataSourceName);
        }

        //如果connections多于想要的connectionSize，则只获取所需部分
        List&lt;Connection&gt; result;
        if (connections.size() &gt;= connectionSize) {
            result = new ArrayList&lt;&gt;(connections).subList(0, connectionSize);
        } else if (!connections.isEmpty()) {//如果connections不够
            result = new ArrayList&lt;&gt;(connectionSize);
            result.addAll(connections);
            //创建新的connections
            List&lt;Connection&gt; newConnections = createConnections(dataSourceName, connectionMode, dataSource, connectionSize - connections.size());
            result.addAll(newConnections);
            synchronized (cachedConnections) {
                //将新创建的connections也放入缓存中进行管理
                cachedConnections.putAll(dataSourceName, newConnections);
            }
        } else {//如果缓存中没有对应dataSource的Connections，同样进行创建并放入缓存中
            result = new ArrayList&lt;&gt;(createConnections(dataSourceName, connectionMode, dataSource, connectionSize));
            synchronized (cachedConnections) {
                cachedConnections.putAll(dataSourceName, result);
            }
        }
        return result;
}
</code></pre>
<p>这段代码有三个判断，流程上比较简单，参考注释即可，需要关注的是其中的 createConnections 方法：</p>
<pre><code>private List&lt;Connection&gt; createConnections(final String dataSourceName, final ConnectionMode connectionMode, final DataSource dataSource, final int connectionSize) throws SQLException {
        if (1 == connectionSize) {
            Connection connection = createConnection(dataSourceName, dataSource);
            replayMethodsInvocation(connection);
            return Collections.singletonList(connection);
        }
        if (ConnectionMode.CONNECTION_STRICTLY == connectionMode) {
            return createConnections(dataSourceName, dataSource, connectionSize);
        }
        synchronized (dataSource) {
            return createConnections(dataSourceName, dataSource, connectionSize);
        }
}
</code></pre>
<p>这段代码涉及了 ConnectionMode（连接模式），这是 ShardingSphere 执行引擎中的重要概念，今天我们先不展开，将在第 21 课时“执行引擎：分片环境下SQL执行的整体流程应该如何进行抽象？”中详细讲解。这里，可以看到 createConnections 方法批量调用了一个 createConnection 抽象方法，该方法需要 AbstractConnectionAdapter 的子类进行实现：</p>
<pre><code>protected abstract Connection createConnection(String dataSourceName, DataSource dataSource) throws SQLException;
</code></pre>
<p>同时，我们看到对于创建的 Connection 对象，都需要执行这样一个语句：</p>
<pre><code>replayMethodsInvocation(connection);
</code></pre>
<p>这行代码比较难以理解，让我们来到定义它的地方，即 WrapperAdapter 类。</p>
<h4>WrapperAdapter</h4>
<p>从命名上看，WrapperAdapter 是一个包装器的适配类，实现了 JDBC 中的 Wrapper 接口。我们在该类中找到了这样一对方法定义：</p>
<pre><code>    //记录方法调用
    public final void recordMethodInvocation(final Class&lt;?&gt; targetClass, final String methodName, final Class&lt;?&gt;[] argumentTypes, final Object[] arguments) {
        jdbcMethodInvocations.add(new JdbcMethodInvocation(targetClass.getMethod(methodName, argumentTypes), arguments));
	}
	 
	//重放方法调用
    public final void replayMethodsInvocation(final Object target) {
        for (JdbcMethodInvocation each : jdbcMethodInvocations) {
            each.invoke(target);
        }
	}
</code></pre>
<p>这两个方法都用到了 JdbcMethodInvocation 类：</p>
<pre><code>public class JdbcMethodInvocation {

    @Getter
    private final Method method;

    @Getter
    private final Object[] arguments;

    public void invoke(final Object target) {
        method.invoke(target, arguments);
    }
}
</code></pre>
<p>显然，JdbcMethodInvocation 类中用到了反射技术根据传入的 method 和 arguments 对象执行对应方法。</p>
<p>了解了 JdbcMethodInvocation 类的原理后，我们就不难理解 recordMethodInvocation 和 replayMethodsInvocation 方法的作用。其中，recordMethodInvocation 用于记录需要执行的方法和参数，而 replayMethodsInvocation 则根据这些方法和参数通过反射技术进行执行。</p>
<p>对于执行 replayMethodsInvocation，我们必须先找到 recordMethodInvocation 的调用入口。通过代码的调用关系，可以看到在 AbstractConnectionAdapter 中对其进行了调用，具体来说就是 setAutoCommit、setReadOnly 和 setTransactionIsolation 这三处方法。这里以 setReadOnly 方法为例给出它的实现：</p>
<pre><code>    @Override
    public final void setReadOnly(final boolean readOnly) throws SQLException {
        this.readOnly = readOnly; 
        //调用recordMethodInvocation方法记录方法调用的元数据
        recordMethodInvocation(Connection.class, &quot;setReadOnly&quot;, new Class[]{boolean.class}, new Object[]{readOnly});

        //执行回调
        forceExecuteTemplate.execute(cachedConnections.values(), new ForceExecuteCallback&lt;Connection&gt;() {

            @Override
            public void execute(final Connection connection) throws SQLException {
                connection.setReadOnly(readOnly);
            }
        });
    }
</code></pre>
<h4>AbstractUnsupportedOperationConnection</h4>
<p>另一方面，从类层关系上，可以看到 AbstractConnectionAdapter 直接继承的是 AbstractUnsupportedOperationConnection 而不是 WrapperAdapter，而在 AbstractUnsupportedOperationConnection 中都是一组直接抛出异常的方法。这里截取部分代码：</p>
<pre><code>public abstract class AbstractUnsupportedOperationConnection extends WrapperAdapter implements Connection {

    @Override
    public final CallableStatement prepareCall(final String sql) throws SQLException {
        throw new SQLFeatureNotSupportedException(&quot;prepareCall&quot;);
    }

    @Override
    public final CallableStatement prepareCall(final String sql, final int resultSetType, final int resultSetConcurrency) throws SQLException {
        throw new SQLFeatureNotSupportedException(&quot;prepareCall&quot;);
}
…
}
</code></pre>
<p>AbstractUnsupportedOperationConnection 这种处理方式的目的就是明确哪些操作是 AbstractConnectionAdapter 及其子类 ShardingConnection 所不能支持的，属于职责分离的一种具体实现方法。</p>
<h3>小结</h3>
<p>JDBC 规范是理解和应用 ShardingSphere 的基础，ShardingSphere 对 JDBC 规范进行了重写，并提供了完全兼容的一套接口。在这一课时中，我们首先给出了 JDBC 规范中各个核心接口的介绍；正是在这些接口的基础上，ShardingSphere 基于适配器模式对 JDBC 规范进行了重写；我们对这一重写方案进行了抽象，并基于 ShardingConnectin 类的实现过程详细阐述了 ShardingSphere 重写 Connection 接口的源码分析。</p>
<p>这里给你留一道思考题：ShardingSphere如何基于适配器模式实现对JDBC中核心类的重写？</p>
<p>JDBC 规范与 ShardingSphere 的兼容性概念至关重要。在掌握了这个概念之后，下一课时将介绍应用集成方面的话题，即在业务系统中使用 ShardingSphere 的具体方式。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="02&#32;&#32;顶级项目：ShardingSphere&#32;是一款什么样的&#32;Apache&#32;开源软件？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="04&#32;&#32;应用集成：在业务系统中使用&#32;ShardingSphere&#32;的方式有哪些？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434c0b7d9370ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ShardingSphere%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86%E7%B2%BE%E8%AE%B2-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
