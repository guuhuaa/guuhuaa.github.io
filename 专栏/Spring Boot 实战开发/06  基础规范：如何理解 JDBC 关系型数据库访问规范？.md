<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>06  基础规范：如何理解 JDBC 关系型数据库访问规范？.md</title>
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

                    <a class="current-tab" href="06&#32;&#32;基础规范：如何理解&#32;JDBC&#32;关系型数据库访问规范？.md">06  基础规范：如何理解 JDBC 关系型数据库访问规范？.md</a>
                    

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
                        <div><h1>06  基础规范：如何理解 JDBC 关系型数据库访问规范？</h1>
<p>从今天开始，我们将进入 Spring Boot 另一个核心技术体系的讨论，即数据访问技术体系。无论是互联网应用还是传统软件，对于任何一个系统而言，数据的存储和访问都是不可缺少的。</p>
<p>数据访问层的构建可能会涉及多种不同形式的数据存储媒介，本课程关注的是最基础也是最常用的数据存储媒介，即关系型数据库，针对关系型数据库，Java 中应用最广泛的就是 JDBC 规范，今天我们将对这个经典规范展开讨论。</p>
<p>JDBC 是 Java Database Connectivity 的全称，它的设计初衷是提供一套能够应用于各种数据库的统一标准，这套标准需要不同数据库厂家之间共同遵守，并提供各自的实现方案供 JDBC 应用程序调用。</p>
<p>作为一套统一标准，JDBC 规范具备完整的架构体系，如下图所示：</p>
<p><img src="assets/CgqCHl_J3f2AMaTEAADODtTLjeA995.png" alt="Drawing 2.png" /></p>
<p>JDBC 规范整体架构图</p>
<p>从上图中可以看到，Java 应用程序通过 JDBC 所提供的 API 进行数据访问，而这些 API 中包含了开发人员所需要掌握的各个核心编程对象，下面我们一起来看下。</p>
<h3>JDBC 规范中有哪些核心编程对象？</h3>
<p>对于日常开发而言，JDBC 规范中的核心编程对象包括 DriverManger、DataSource、Connection、Statement，及 ResultSet。</p>
<h4>DriverManager</h4>
<p>正如前面的 JDBC 规范整体架构图中所示，JDBC 中的 DriverManager 主要负责加载各种不同的驱动程序（Driver），并根据不同的请求向应用程序返回相应的数据库连接（Connection），应用程序再通过调用 JDBC API 实现对数据库的操作。</p>
<p>JDBC 中的 Driver 定义如下，其中最重要的是第一个获取 Connection 的 connect 方法：</p>
<pre><code>public interface Driver {

    //获取数据库连接

    Connection connect(String url, java.util.Properties info)

        throws SQLException;

    boolean acceptsURL(String url) throws SQLException;

    DriverPropertyInfo[] getPropertyInfo(String url, java.util.Properties info)

                         throws SQLException;

    int getMajorVersion();

    int getMinorVersion();

    boolean jdbcCompliant();

    public Logger getParentLogger() throws SQLFeatureNotSupportedException;

}
</code></pre>
<p>针对 Driver 接口，不同的数据库供应商分别提供了自身的实现方案。例如，MySQL 中的 Driver 实现类如下代码所示：</p>
<pre><code>public class Driver extends NonRegisteringDriver implements java.sql.Driver {

    // 通过 DriverManager 注册 Driver

    static {

        try {

            java.sql.DriverManager.registerDriver(new Driver());

        } catch (SQLException E) {

            throw new RuntimeException(&quot;Can't register driver!&quot;);

        }

	}

	…

}
</code></pre>
<p>这里就使用用了 DriverManager，而 DriverManager 除提供了上述用于注册 Driver 的 registerDriver 方法之外，还提供了 getConnection 方法用于针对具体的 Driver 获取 Connection 对象。</p>
<h4>DataSource</h4>
<p>通过前面的介绍，我们知道在 JDBC 规范中可直接通过 DriverManager 获取 Connection，我们也知道获取 Connection 的过程需要建立与数据库之间的连接，而这个过程会产生较大的系统开销。</p>
<p>为了提高性能，通常我们首先会建立一个中间层将 DriverManager 生成的 Connection 存放到连接池中，再从池中获取 Connection。</p>
<p>而我们可以认为 DataSource 就是这样一个中间层，它作为 DriverManager 的替代品而推出，是获取数据库连接的首选方法。</p>
<p>DataSource 在 JDBC 规范中代表的是一种数据源，核心作用是获取数据库连接对象 Connection。在日常开发过程中，我们通常会基于 DataSource 获取 Connection。DataSource 接口的定义如下代码所示：</p>
<pre><code>public interface DataSource  extends CommonDataSource, Wrapper {

 

  Connection getConnection() throws SQLException;

 

  Connection getConnection(String username, String password)

    throws SQLException;

}
</code></pre>
<p>从上面我们可以看到，DataSource 接口提供了两个获取 Connection 的重载方法，并继承了 CommonDataSource 接口。CommonDataSource 是 JDBC 中关于数据源定义的根接口，除了 DataSource 接口之外，它还有另外两个子接口，如下图所示：</p>
<p><img src="assets/CgpVE1_9BRyALcLiAACsqMysPwQ396.png" alt="图片3.png" /></p>
<p>DataSource 类层结构图</p>
<p>其中，DataSource 是官方定义的获取 Connection 的基础接口，XADataSource 用来在分布式事务环境下实现 Connection 的获取，而 ConnectionPoolDataSource 是从连接池 ConnectionPool 中获取 Connection 的接口。</p>
<p>所谓的 ConnectionPool 相当于预先生成一批 Connection 并存放在池中，从而提升 Connection 获取的效率。</p>
<p>请注意 DataSource 接口同时还继承了一个 Wrapper 接口。从接口的命名上看，我们可以判断该接口起到一种包装器的作用。事实上，因为很多数据库供应商提供了超越标准 JDBC API 的扩展功能，所以 Wrapper 接口可以把一个由第三方供应商提供的、非 JDBC 标准的接口包装成标准接口。</p>
<p>以 DataSource 接口为例，如果我们想自己实现一个定制化的数据源类 MyDataSource，就可以提供一个实现了 Wrapper 接口的 MyDataSourceWrapper 类来完成包装和适配，如下图所示：</p>
<p><img src="assets/Cgp9HWB8_iWABX6dAAC2_bCPSoQ200.png" alt="图片4.png" /></p>
<p>通过 Wrapper 接口扩展 JDBC 规范示意图</p>
<p>在 JDBC 规范中，除了 DataSource 之外，Connection、Statement、ResultSet 等核心对象也都继承了这个 Wrapper 接口。</p>
<p>作为一种基础组件，它同样不需要开发人员自己实现 DataSource，因为业界已经存在了很多优秀的实现方案，如 DBCP、C3P0 和 Druid 等。</p>
<p>例如 Druid 提供了 DruidDataSource，它不仅提供了连接池的功能，还提供了诸如监控等其他功能，它的类层结构如下图所示：</p>
<p><img src="assets/CgpVE1_9BS-AEQNBAABgakhN868633.png" alt="图片5.png" /></p>
<p>DruidDataSource 的类层结构</p>
<h4>Connection</h4>
<p>DataSource 的目的是获取 Connection 对象。我们可以把 Connection 理解为一种会话（Session）机制，Connection 代表一个数据库连接，负责完成与数据库之间的通信。</p>
<p>所有 SQL 的执行都是在某个特定 Connection 环境中进行的，同时它还提供了一组重载方法分别用于创建 Statement 和 PreparedStatement。另一方面，Connection 也涉及事务相关的操作。</p>
<p>Connection 接口中定义的方法很丰富，其中最核心的几个方法如下代码所示：</p>
<pre><code>public interface Connection  extends Wrapper, AutoCloseable {

	//创建 Statement

	Statement createStatement() throws SQLException;

	//创建 PreparedStatement

	PreparedStatement prepareStatement(String sql) throws SQLException;

	//提交

	void commit() throws SQLException;

	//回滚

	void rollback() throws SQLException;

	//关闭连接

	void close() throws SQLException;

}
</code></pre>
<p>这里涉及具体负责执行 SQL 语句的 Statement 和 PreparedStatement 对象，我们接着往下看。</p>
<h4>Statement/PreparedStatement</h4>
<p>JDBC 规范中的 Statement 存在两种类型，一种是普通的 Statement，一种是支持预编译的 PreparedStatement。</p>
<p>所谓预编译，是指数据库的编译器会对 SQL 语句提前编译，然后将预编译的结果缓存到数据库中，下次执行时就可以通过替换参数并直接使用编译过的语句，从而大大提高 SQL 的执行效率。</p>
<p>当然，这种预编译也需要一定成本，因此在日常开发中，如果对数据库只执行一次性读写操作时，用 Statement 对象进行处理会比较合适；而涉及 SQL 语句的多次执行时，我们可以使用 PreparedStatement。</p>
<p>如果需要查询数据库中的数据，我们只需要调用 Statement 或 PreparedStatement 对象的 executeQuery 方法即可。</p>
<p>这个方法以 SQL 语句作为参数，执行完后返回一个 JDBC 的 ResultSet 对象。当然，Statement 或 PreparedStatement 还提供了一大批执行 SQL 更新和查询的重载方法，我们无意一一展开。</p>
<p>以 Statement 为例，它的核心方法如下代码所示：</p>
<pre><code>public interface Statement extends Wrapper, AutoCloseable {

	//执行查询语句

	ResultSet executeQuery(String sql) throws SQLException; 

	//执行更新语句

	int executeUpdate(String sql) throws SQLException; 

	//执行 SQL 语句

	boolean execute(String sql) throws SQLException; 

	//执行批处理

    int[] executeBatch() throws SQLException;

}
</code></pre>
<p>这里我们同样引出了 JDBC 规范中最后一个核心编程对象，即代表执行结果的 ResultSet。</p>
<h4>ResultSet</h4>
<p>一旦我们通过 Statement 或 PreparedStatement 执行了 SQL 语句并获得了 ResultSet 对象，就可以使用该对象中定义的一大批用于获取 SQL 执行结果值的工具方法，如下代码所示：</p>
<pre><code>public interface ResultSet extends Wrapper, AutoCloseable {

	//获取下一个结果

	boolean next() throws SQLException;

	//获取某一个类型的结果值

	Value getXXX(int columnIndex) throws SQLException;

	…

}
</code></pre>
<p>ResultSet 提供了 next() 方法便于开发人员实现对整个结果集的遍历。如果 next() 方法返回为 true，意味着结果集中存在数据，可以调用 ResultSet 对象的一系列 getXXX() 方法来取得对应的结果值。</p>
<h3>如何使用 JDBC 规范访问数据库？</h3>
<p>对于开发人员而言，JDBC API 是我们访问数据库的主要途径，如果我们使用 JDBC 开发一个访问数据库的执行流程，常见的代码风格如下所示（省略了异常处理）：</p>
<pre><code>// 创建池化的数据源

PooledDataSource dataSource = new PooledDataSource ();

// 设置 MySQL Driver

dataSource.setDriver (&quot;com.mysql.jdbc.Driver&quot;);

// 设置数据库 URL、用户名和密码

dataSource.setUrl (&quot;jdbc:mysql://localhost:3306/test&quot;);

dataSource.setUsername(&quot;root&quot;);

dataSource.setPassword(&quot;root&quot;);

// 获取连接

Connection connection = dataSource.getConnection();

 

// 执行查询

PreparedStatement statement = connection.prepareStatement (&quot;select * from user&quot;);

// 获取查询结果进行处理

ResultSet resultSet = statement.executeQuery();

while (resultSet.next()) {

	…

}

 

// 关闭资源

statement.close();

resultSet.close();

connection.close();
</code></pre>
<p>这段代码中完成了对基于前面介绍的 JDBC API 中的各个核心编程对象的数据访问。上述代码主要面向查询场景，而针对用于插入数据的处理场景，我们只需要在上述代码中替换几行代码，即将“执行查询”和“获取查询结果进行处理”部分的查询操作代码替换为插入操作代码就行。</p>
<p>最后，我们梳理一下基于 JDBC 规范进行数据库访问的整个开发流程，如下图所示：</p>
<p><img src="assets/Ciqc1F_J3jmANBxqAADebgJ5BdU438.png" alt="Drawing 10.png" /></p>
<p>基于 JDBC 规范进行数据库访问的开发流程图</p>
<p>针对前面所介绍的代码示例，我们明确地将基于 JDBC 规范访问关系型数据库的操作分成两大部分：一部分是准备和释放资源以及执行 SQL 语句，另一部分则是处理 SQL 执行结果。</p>
<p>而对于任何数据访问而言，前者实际上都是重复的。在上图所示的整个开发流程中，事实上只有“处理 ResultSet ”部分的代码需要开发人员根据具体的业务对象进行定制化处理。这种抽象为整个执行过程提供了优化空间。诸如 Spring 框架中 JdbcTemplate 这样的模板工具类就应运而生了，我们会在 07 讲中会详细介绍这个模板工具类。</p>
<h3>小结与预告</h3>
<p>JDBC 规范是 Java EE 领域中进行数据库访问的标准规范，在业界应用非常广泛。今天的课程中，我们分析了该规范的核心编程对象，并梳理了使用 JDBC 规范访问数据库的开发流程。希望你能熟练掌握这部分知识，因为熟练掌握 JDBC 规范是我们理解后续内容的基础。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="05&#32;&#32;自动配置：如何正确理解&#32;Spring&#32;Boot&#32;自动配置实现原理？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="07&#32;&#32;数据访问：如何使用&#32;JdbcTemplate&#32;访问关系型数据库？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434cf67e0b70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
