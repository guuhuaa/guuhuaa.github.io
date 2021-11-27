<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>16  StatementHandler：参数绑定、SQL 执行和结果映射的奠基者.md</title>
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

                    <a class="current-tab" href="16&#32;&#32;StatementHandler：参数绑定、SQL&#32;执行和结果映射的奠基者.md">16  StatementHandler：参数绑定、SQL 执行和结果映射的奠基者.md</a>
                    

                </li>
                <li>

                    
                    <a href="17&#32;&#32;Executor&#32;才是执行&#32;SQL&#32;语句的幕后推手（上）.md">17  Executor 才是执行 SQL 语句的幕后推手（上）.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;Executor&#32;才是执行&#32;SQL&#32;语句的幕后推手（下）.md">18  Executor 才是执行 SQL 语句的幕后推手（下）.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;深入&#32;MyBatis&#32;内核与业务逻辑的桥梁——接口层.md">19  深入 MyBatis 内核与业务逻辑的桥梁——接口层.md</a>

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
                        <div><h1>16  StatementHandler：参数绑定、SQL 执行和结果映射的奠基者</h1>
<p><strong>StatementHandler 接口是 MyBatis 中非常重要的一个接口</strong>，其实现类完成 SQL 语句执行中最核心的一系列操作，这也是后面我们要介绍的 Executor 接口实现的基础。</p>
<p>StatementHandler 接口的定义如下图所示：</p>
<p><img src="assets/Cgp9HWBRyPSAPnqwAADa0tXnYqQ008.png" alt="Drawing 0.png" /></p>
<p>StatementHandler 接口中定义的方法</p>
<p>可以看到，其中提供了创建 Statement 对象（prepare() 方法）、为 SQL 语句绑定实参（parameterize() 方法）、执行单条 SQL 语句（query() 方法和 update() 方法）、批量执行 SQL 语句（batch() 方法）等多种功能。</p>
<p>下图展示了 MyBatis 中提供的所有 StatementHandler 接口实现类，以及它们的继承关系：</p>
<p><img src="assets/Cgp9HWBR0IaAXG4BAAGLvM_7w1Y255.png" alt="图片3.png" /></p>
<p>StatementHandler 接口继承关系图</p>
<p>今天这一讲我们就来详细分析该继承关系图中每个 StatementHandler 实现的核心逻辑。</p>
<h3>RoutingStatementHandler</h3>
<p>RoutingStatementHandler 这个 StatementHandler 实现，有点<strong>策略模式</strong>的意味。在 RoutingStatementHandler 的构造方法中，会根据 MappedStatement 中的 statementType 字段值，选择相应的 StatementHandler 实现进行创建，这个新建的 StatementHandler 对象由 RoutingStatementHandler 中的 delegate 字段维护。</p>
<p>RoutingStatementHandler 的构造方法如下：</p>
<pre><code>public RoutingStatementHandler(Executor executor, MappedStatement ms, Object parameter, RowBounds rowBounds, ResultHandler resultHandler, BoundSql boundSql) {

    // 下面就是根据MappedStatement的配置，生成一个相应的StatementHandler对

    // 象，并设置到delegate字段中维护

    switch (ms.getStatementType()) {

        case STATEMENT:

            // 创建SimpleStatementHandler对象

            delegate = new SimpleStatementHandler(executor, ms, parameter, rowBounds, resultHandler, boundSql);

            break;

        case PREPARED:

            // 创建PreparedStatementHandler对象

            delegate = new PreparedStatementHandler(executor, ms, parameter, rowBounds, resultHandler, boundSql);

            break;

        case CALLABLE:

            // 创建CallableStatementHandler对象

            delegate = new CallableStatementHandler(executor, ms, parameter, rowBounds, resultHandler, boundSql);

            break;

        default: // 抛出异常

            throw new ExecutorException(&quot;...&quot;);

    }

}
</code></pre>
<p>在 RoutingStatementHandler 的其他方法中，<strong>都会委托给底层的 delegate 对象来完成具体的逻辑</strong>。</p>
<h3>BaseStatementHandler</h3>
<p>作为一个抽象类，BaseStatementHandler 只实现了 StatementHandler 接口的 prepare() 方法，其 prepare() 方法实现为新建的 Statement 对象设置了一些参数，例如，timeout、fetchSize 等。BaseStatementHandler 还新增了一个 instantiateStatement() 抽象方法给子类实现，来完成 Statement 对象的其他初始化操作。不过，BaseStatementHandler 中并没有实现 StatementHandler 接口中的数据库操作等核心方法。</p>
<p>了解了 BaseStatementHandler 对 StatementHandler 接口的实现情况之后，我们再来看一下 BaseStatementHandler 的构造方法，其中会<strong>初始化执行 SQL 需要的 Executor 对象</strong>、<strong>为 SQL 绑定实参的 ParameterHandler 对象</strong>以及<strong>生成结果对象的 ResultSetHandler 对象</strong>。这三个核心对象中，ResultSetHandler 对象我们已经在[《14 | 探究 MyBatis 结果集映射机制背后的秘密（上）》]中介绍过了，ParameterHandler 和 Executor 在后面会展开介绍。</p>
<h4>1. KeyGenerator</h4>
<p>这里需要关注的是 generateKeys() 方法，其中会<strong>通过 KeyGenerator 接口生成主键</strong>，下面我们就来看看 KeyGenerator 接口的相关内容。</p>
<p>我们知道不同数据库的自增 id 生成策略并不完全一样。例如，我们常见的 Oracle DB 是通过sequence 实现自增 id 的，如果使用自增 id 作为主键，就需要我们先获取到这个自增的 id 值，然后再使用；MySQL 在使用自增 id 作为主键的时候，insert 语句中可以不指定主键，在插入过程中由 MySQL 自动生成 id。KeyGenerator 接口支持 insert 语句执行前后获取自增的 id，分别对应 processBefore() 方法和 processAfter() 方法，下图展示了 MyBatis 提供的两个 KeyGenerator 接口实现：</p>
<p><img src="assets/Cgp9HWBR0HmAAYIQAAE2FEB8sfU102.png" alt="图片4.png" /></p>
<p>KeyGenerator 接口继承关系图</p>
<p><strong>Jdbc3KeyGenerator 用于获取数据库生成的自增 id（例如 MySQL 那种生成模式）</strong>，其 processBefore() 方法是空实现，processAfter() 方法会将 insert 语句执行后生成的主键保存到用户传递的实参中。我们在使用 MyBatis 执行单行 insert 语句时，一般传入的实参是一个 POJO 对象或是 Map 对象，生成的主键会设置到对应的属性中；执行多条 insert 语句时，一般传入实参是 POJO 对象集合或 Map 对象的数组或集合，集合中每一个元素都对应一次插入操作，生成的多个自增 id 也会设置到每个元素的相应属性中。</p>
<p>Jdbc3KeyGenerator 中获取数据库自增 id 的核心代码片段如下：</p>
<pre><code>// 将数据库生成的自增id作为结果集返回

try (ResultSet rs = stmt.getGeneratedKeys()) { 

    final ResultSetMetaData rsmd = rs.getMetaData();

    final Configuration configuration = ms.getConfiguration();

    if (rsmd.getColumnCount() &lt; keyProperties.length) {

    } else {

        // 处理rs这个结果集，将生成的id设置到对应的属性中

        assignKeys(configuration, rs, rsmd, keyProperties, parameter);

    }

} catch (Exception e) {

    throw new ExecutorException(&quot;...&quot;);

}
</code></pre>
<p><strong>如果使用像 Oracle 这种不支持自动生成主键自增 id 的数据库时，我们可以使用 SelectkeyGenerator 来生成主键 id</strong>。Mapper 映射文件中的<code>&lt;selectKey&gt;</code>标签会被解析成 SelectkeyGenerator 对象，其中的 executeBefore 属性（boolean 类型）决定了是在 insert 语句执行之前获取主键，还是在 insert 语句执行之后获取主键 id。</p>
<p>SelectkeyGenerator 中的 processBefore() 方法和 processAfter() 方法都是通过 processGeneratedKeys() 这个私有方法获取主键 id 的，processGeneratedKeys() 方法会执行<code>&lt;selectKey&gt;</code>标签中指定的 select 语句，查询主键信息，并记录到用户传入的实参对象的对应属性中，核心代码片段如下所示：</p>
<pre><code>// 创建一个新的Executor对象来执行指定的select语句

Executor keyExecutor = configuration.newExecutor(executor.getTransaction(), ExecutorType.SIMPLE);

// 拿到主键信息

List&lt;Object&gt; values = keyExecutor.query(keyStatement, parameter, RowBounds.DEFAULT, Executor.NO_RESULT_HANDLER);

if (values.size() == 0) {

    throw new ExecutorException(&quot;SelectKey returned no data.&quot;);

} else if (values.size() &gt; 1) {

    throw new ExecutorException(&quot;SelectKey returned more than one value.&quot;);

} else {

    // 创建实参对象的MetaObject对象

    final MetaObject metaParam = configuration.newMetaObject(parameter);

    MetaObject metaResult = configuration.newMetaObject(values.get(0));

    if (keyProperties.length == 1) {

        // 将主键信息记录到用户传入的实参对象中

        if (metaResult.hasGetter(keyProperties[0])) {

            setValue(metaParam, keyProperties[0], metaResult.getValue(keyProperties[0]));

        } else {

            setValue(metaParam, keyProperties[0], values.get(0));

        }

    } else {

        ... // 多结果集的处理

    }

}
</code></pre>
<h4>2. ParameterHandler</h4>
<p>介绍完 KeyGenerator 接口之后，我们再来看一下 BaseStatementHandler 中依赖的另一个辅助类—— ParameterHandler。</p>
<p>经过前面[《13 | 深入分析动态 SQL 语句解析全流程（下）》]介绍的一系列 SqlNode 的处理之后，我们得到的 SQL 语句（维护在 BoundSql 对象中）可能包含多个“?”占位符，与此同时，用于替换每个“?”占位符的实参都记录在 BoundSql.parameterMappings 集合中。</p>
<p>ParameterHandler 接口中定义了两个方法：一个是 getParameterObject() 方法，用来获取传入的实参对象；另一个是 setParameters() 方法，用来替换“?”占位符，这是 ParameterHandler 的<strong>核心方法</strong>。</p>
<p><strong>DefaultParameterHandler 是 ParameterHandler 接口的唯一实现，其 setParameters() 方法会遍历 BoundSql.parameterMappings 集合</strong>，根据参数名称查找相应实参，最后会通过 PreparedStatement.set*() 方法与 SQL 语句进行绑定。setParameters() 方法的具体代码如下：</p>
<pre><code>for (int i = 0; i &lt; parameterMappings.size(); i++) {

    ParameterMapping parameterMapping = parameterMappings.get(i);

    Object value;

    String propertyName = parameterMapping.getProperty();

    // 获取实参值

    if (boundSql.hasAdditionalParameter(propertyName)) {

        value = boundSql.getAdditionalParameter(propertyName);

    } else if (parameterObject == null) {

        value = null;

    } else if (typeHandlerRegistry.hasTypeHandler(parameterObject.getClass())) {

        value = parameterObject;

    } else {

        MetaObject metaObject = configuration.newMetaObject(parameterObject);

        value = metaObject.getValue(propertyName);

    }

    // 获取TypeHandler

    TypeHandler typeHandler = parameterMapping.getTypeHandler();

    JdbcType jdbcType = parameterMapping.getJdbcType();

    // 底层会调用PreparedStatement.set*()方法完成绑定

    typeHandler.setParameter(ps, i + 1, value, jdbcType);

}
</code></pre>
<h3>SimpleStatementHandler</h3>
<p>SimpleStatementHandler 是 StatementHandler 的具体实现之一，继承了 BaseStatementHandler 抽象类。SimpleStatementHandler 各个方法接收的是 java.sql.Statement 对象，并通过该对象来完成 CRUD 操作，所以在 SimpleStatementHandler 中<strong>维护的 SQL 语句不能存在“?”占位符</strong>，填充占位符的 parameterize() 方法也是空实现。</p>
<p>在 instantiateStatement() 这个初始化方法中，SimpleStatementHandler 会直接通过 JDBC Connection 创建 Statement 对象，这个对象也是后续 SimpleStatementHandler 其他方法的入参。</p>
<p>在 query() 方法实现中，SimpleStatementHandler 会直接通过上面创建的 Statement 对象，执行 SQL 语句，返回的结果集由 ResultSetHandler 完成映射，核心代码如下：</p>
<pre><code>public &lt;E&gt; List&lt;E&gt; query(Statement statement, ResultHandler resultHandler) throws SQLException {、

    // 获取SQL语句

    String sql = boundSql.getSql();

    // 执行SQL语句

    statement.execute(sql);

    // 处理ResultSet映射，得到结果对象

    return resultSetHandler.handleResultSets(statement);

}
</code></pre>
<p>queryCursor() 方法与 query() 方法实现类似，这里就不再赘述。</p>
<p>batch() 方法调用的是 Statement.addBatch() 方法添加批量执行的 SQL 语句，但并不是立即执行，而是等待 Statement.executeBatch() 方法执行时才会批量执行，这点你稍微注意一下即可。</p>
<p>至于 update() 方法，首先会通过 Statement.execute() 方法执行 insert、update 或 delete 类型的 SQL 语句，然后执行 KeyGenerator.processAfter() 方法查询主键并填充相应属性（processBefore() 方法已经在 prepare() 方法中执行过了），最后通过 Statement.getUpdateCount() 方法获取 SQL 语句影响的行数并返回。</p>
<h3>PreparedStatementHandler</h3>
<p>PreparedStatementHandler 是 StatementHandler 的具体实现之一，也是最常用的 StatementHandler 实现，它同样继承了 BaseStatementHandler 抽象类。PreparedStatementHandler 各个方法接收的是 java.sql.PreparedStatement 对象，并通过该对象来完成 CRUD 操作，在其 parameterize() 方法中会通过前面介绍的 ParameterHandler调用 PreparedStatement.set*() 方法为 SQL 语句绑定参数，所以在 PreparedStatementHandler 中<strong>维护的 SQL 语句是可以包含“?”占位符的</strong>。</p>
<p>在 instantiateStatement() 方法中，PreparedStatementHandler 会直接通过 JDBC Connection 的 prepareStatement() 方法创建 PreparedStatement 对象，该对象就是 PreparedStatementHandler 其他方法的入参。</p>
<p>PreparedStatementHandler 的 query() 方法、batch() 方法以及 update() 方法与 SimpleStatementHandler 的实现基本相同，只不过是把 Statement API 换成了 PrepareStatement API 而已。下面我们以 update() 方法为例进行简单介绍：</p>
<pre><code>public int update(Statement statement) throws SQLException {

    PreparedStatement ps = (PreparedStatement) statement;

    ps.execute(); // 执行SQL语句，修改数据

    int rows = ps.getUpdateCount(); // 获取影响行数

    // 获取实参对象

    Object parameterObject = boundSql.getParameterObject();

    // 执行KeyGenerator

    KeyGenerator keyGenerator = mappedStatement.getKeyGenerator();

    keyGenerator.processAfter(executor, mappedStatement, ps, parameterObject);

    return rows; // 返回影响行数

}
</code></pre>
<h3>CallableStatementHandler</h3>
<p><strong>CallableStatementHandler 是处理存储过程的 StatementHandler 实现</strong>，其 instantiateStatement() 方法会通过 JDBC Connection 的 prepareCall() 方法为指定存储过程创建对应的 java.sql.CallableStatement 对象。在 parameterize() 方法中，CallableStatementHandler 除了会通过 ParameterHandler 完成实参的绑定之外，还会指定输出参数的位置和类型。</p>
<p>在 CallableStatementHandler 的 query()、queryCursor()、update() 方法中，除了处理 SQL 语句本身的结果集（ResultSet 结果集或是影响行数），还会通过 ResultSetHandler 的 handleOutputParameters() 方法处理输出参数，这是与 PreparedStatementHandler 最大的不同。下面我们以 query() 方法为例进行简单分析：</p>
<pre><code>public &lt;E&gt; List&lt;E&gt; query(Statement statement, ResultHandler resultHandler) throws SQLException {

    CallableStatement cs = (CallableStatement) statement;

    cs.execute(); // 执行存储过程

    // 处理存储过程返回的结果集

    List&lt;E&gt; resultList = resultSetHandler.handleResultSets(cs);

    // 处理输出参数，可能修改resultList集合

    resultSetHandler.handleOutputParameters(cs);

    // 返回最后的结果对象

    return resultList;

}
</code></pre>
<h3>总结</h3>
<p>这一讲我们重点讲解了 MyBatis 中的 StatementHandler 接口及其核心实现，StatementHandler 接口中定义了执行一条 SQL 语句的核心方法。</p>
<ul>
<li>首先，分析了 RoutingStatementHandler 实现，它可以帮助我们选择真正的 StatementHandler 实现类。</li>
<li>接下来，介绍了 BaseStatementHandler 这个抽象类的实现，同时还详细阐述了其中使用到的 KeyGenerator 和 ParameterHandler。</li>
<li>最后，又介绍了 SimpleStatementHandler、PreparedStatementHandler 等实现，它们基于 JDBC API 接口，实现了完整的 StatementHandler 功能。</li>
</ul>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="15&#32;&#32;探究&#32;MyBatis&#32;结果集映射机制背后的秘密（下）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="17&#32;&#32;Executor&#32;才是执行&#32;SQL&#32;语句的幕后推手（上）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435739a91c645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
