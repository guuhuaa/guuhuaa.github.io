<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>11  鸟瞰 MyBatis 初始化，把握 MyBatis 启动流程脉络（下）.md</title>
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

                    <a class="current-tab" href="11&#32;&#32;鸟瞰&#32;MyBatis&#32;初始化，把握&#32;MyBatis&#32;启动流程脉络（下）.md">11  鸟瞰 MyBatis 初始化，把握 MyBatis 启动流程脉络（下）.md</a>
                    

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
                        <div><h1>11  鸟瞰 MyBatis 初始化，把握 MyBatis 启动流程脉络（下）</h1>
<p>在上一讲，我们深入分析了MyBatis 初始化过程中对 mybatis-config.xml 全局配置文件的解析，详细介绍了其中每个标签的解析流程以及涉及的经典设计模式——构造者模式。这一讲我们就紧接着上一讲的内容，继续介绍 MyBatis 初始化流程，重点介绍Mapper.xml 配置文件的解析以及 SQL 语句的处理逻辑。</p>
<h3>Mapper.xml 映射文件解析全流程</h3>
<p>在上一讲分析 mybatis-config.xml 配置文件解析流程的时候我们看到，在 mybatis-config.xml 配置文件中可以定义多个 <code>&lt;mapper&gt;</code> 标签指定 Mapper 配置文件的地址，<strong>MyBatis 会为每个 Mapper.xml 映射文件创建一个 XMLMapperBuilder 实例完成解析</strong>。</p>
<p>与 XMLConfigBuilder 类似，XMLMapperBuilder也是具体构造者的角色，继承了 BaseBuilder 这个抽象类，解析 Mapper.xml 映射文件的入口是 XMLMapperBuilder.parse() 方法，其核心步骤如下：</p>
<ul>
<li>执行 configurationElement() 方法解析整个Mapper.xml 映射文件的内容；</li>
<li>获取当前 Mapper.xml 映射文件指定的 Mapper 接口，并进行注册；</li>
<li>处理 configurationElement() 方法中解析失败的 <code>&lt;resultMap&gt;</code> 标签；</li>
<li>处理 configurationElement() 方法中解析失败的 <code>&lt;cache-ref&gt;</code> 标签；</li>
<li>处理 configurationElement() 方法中解析失败的SQL 语句标签。</li>
</ul>
<p>可以清晰地看到，<strong>configurationElement() 方法才是真正解析 Mapper.xml 映射文件的地方</strong>，其中定义了处理 Mapper.xml 映射文件的核心流程：</p>
<ul>
<li>获取 <code>&lt;mapper&gt;</code> 标签中的 namespace 属性，同时会进行多种边界检查；</li>
<li>解析 <code>&lt;cache&gt;</code> 标签；</li>
<li>解析 <code>&lt;cache-ref&gt;</code> 标签；</li>
<li>解析 <code>&lt;resultMap&gt;</code> 标签；</li>
<li>解析 <code>&lt;sql&gt;</code> 标签；</li>
<li>解析 <code>&lt;select&gt;</code>、<code>&lt;insert&gt;</code>、<code>&lt;update&gt;</code>、<code>&lt;delete&gt;</code> 等 SQL 标签。</li>
</ul>
<p>下面我们就按照顺序逐一介绍这些方法的核心实现。</p>
<h4>1. 处理 <code>&lt;cache&gt;</code> 标签</h4>
<p>我们知道 Cache 接口及其实现是MyBatis 一级缓存和二级缓存的基础，其中，一级缓存是默认开启的，而二级缓存默认情况下并没有开启，如有需要，<strong>可以通过<cache>标签为指定的namespace 开启二级缓存</strong>。</p>
<p>XMLMapperBuilder 中解析 <code>&lt;cache&gt;</code> 标签的<strong>核心逻辑位于 cacheElement() 方法</strong>之中，其具体步骤如下：</p>
<ul>
<li>获取 <code>&lt;cache&gt;</code> 标签中的各项属性（type、flushInterval、size 等属性）；</li>
<li>读取 <code>&lt;cache&gt;</code> 标签下的子标签信息，这些信息将用于初始化二级缓存；</li>
<li>MapperBuilderAssistant 会根据上述配置信息，创建一个全新的Cache 对象并添加到 Configuration.caches 集合中保存。</li>
</ul>
<p>也就是说，解析 <code>&lt;cache&gt;</code> 标签得到的所有信息将会传给 MapperBuilderAssistant 完成 Cache 对象的创建，创建好的Cache 对象会添加到 Configuration.caches 集合中，<strong>这个 caches 字段是一个StrictMap<Cache> 类型的集合</strong>，其中的 Key是Cache 对象的唯一标识，默认值是Mapper.xml 映射文件的namespace，Value 才是真正的二级缓存对应的 Cache 对象。</p>
<p>这里我们简单介绍一下 StrictMap的特性。</p>
<p>StrictMap 继承了 HashMap，并且覆盖了 HashMap 的一些行为，例如，相较于 HashMap 的 put() 方法，StrictMap 的 put() 方法有如下几点不同：</p>
<ul>
<li>如果检测到重复 Key 的写入，会直接抛出异常；</li>
<li>在没有重复 Key的情况下，会正常写入 KV 数据，与此同时，还会根据 Key产生一个 shortKey，shortKey 与完整 Key 指向同一个 Value 值；</li>
<li>如果 shortKey 已经存在，则将 value 修改成 Ambiguity 对象，Ambiguity 对象表示这个 shortKey 存在二义性，后续通过 StrictMap的get() 方法获取该 shortKey 的时候，会抛出异常。</li>
</ul>
<p>了解了 StrictMap 这个集合类的特性之后，我们回到MapperBuilderAssistant 这个类继续分析，在它的 useNewCache() 方法中，会根据前面解析得到的配置信息，通过 CacheBuilder 创建 Cache 对象。</p>
<p>通过名字你就能猜测到 CacheBuilder 是 Cache 的构造者，<strong>CacheBuilder 中最核心的方法是build() 方法，其中会根据传入的配置信息创建底层存储数据的 Cache 对象以及相关的 Cache 装饰器</strong>，具体实现如下：</p>
<pre><code>public Cache build() {

    // 将implementation默认值设置为PerpetualCache，在decorators集合中默认添加LruCache装饰器，

    // 都是在setDefaultImplementations()方法中完成的

    setDefaultImplementations();

    // 通过反射，初始化implementation指定类型的对象

    Cache cache = newBaseCacheInstance(implementation, id);

    // 创建Cache关联的MetaObject对象，并根据properties设置Cache中的各个字段

    setCacheProperties(cache);

    // 根据上面创建的Cache对象类型，决定是否添加装饰器

    if (PerpetualCache.class.equals(cache.getClass())) {

        // 如果是PerpetualCache类型，则为其添加decorators集合中指定的装饰器

        for (Class&lt;? extends Cache&gt; decorator : decorators) {

            // 通过反射创建Cache装饰器

            cache = newCacheDecoratorInstance(decorator, cache);

            // 依赖MetaObject将properties中配置信息设置到Cache的各个属性中，同时调用Cache的initialize()方法完成初始化

            setCacheProperties(cache);

        }

        // 根据readWrite、blocking、clearInterval等配置，

        // 添加SerializedCache、ScheduledCache等装饰器

        cache = setStandardDecorators(cache);

    } else if (!LoggingCache.class.isAssignableFrom(cache.getClass())) {

        // 如果不是PerpetualCache类型，就是其他自定义类型的Cache，则添加一个LoggingCache装饰器

        cache = new LoggingCache(cache);

    }

    return cache;

}
</code></pre>
<h4>2. 处理<code>&lt;cache-ref&gt;</code>标签</h4>
<p>通过上述介绍我们知道，可以通过 <code>&lt;cache&gt;</code> 标签为每个 namespace 开启二级缓存，同时还会将 namespace 与关联的二级缓存 Cache对象记录到 Configuration.caches 集合中，也就是说二级缓存是 namespace 级别的。但是，在有的场景中，我们会需要在多个 namespace 共享同一个二级缓存，也就是<strong>共享同一个 Cache 对象</strong>。</p>
<p>为了解决这个需求，MyBatis提供了 <code>&lt;cache-ref&gt; </code>标签来引用另一个 namespace 的二级缓存。cacheRefElement() 方法是处理 <code>&lt;cache-ref&gt;</code> 标签的核心逻辑所在，在 Configuration 中维护了一个 cacheRefMap 字段（HashMap&lt;String,String&gt; 类型），其中的 Key 是 <code>&lt;cache-ref&gt;</code> 标签所属的namespace 标识，Value 值是 <code>&lt;cache-ref&gt;</code> 标签引用的 namespace 值，这样的话，就可以将两个namespace 关联起来了，即这两个 namespace 共用一个 Cache对象。</p>
<p>这里会使用到一个叫 CacheRefResolver 的 Cache 引用解析器。<strong>CacheRefResolver 中记录了被引用的 namespace以及当前 namespace 关联的MapperBuilderAssistant 对象</strong>。前面在解析 <code>&lt;cache&gt;</code>标签的时候我们介绍过，MapperBuilderAssistant 会在 useNewCache() 方法中通过 CacheBuilder 创建新的 Cache 对象，并记录到 currentCache 字段。而这里解析 <code>&lt;cache-ref&gt;</code> 标签的时候，MapperBuilderAssistant 会通过 useCacheRef() 方法从 Configuration.caches 集合中，根据被引用的namespace 查找共享的 Cache 对象来初始化 currentCache，而不再创建新的Cache 对象，从而实现二级缓存的共享。</p>
<h4>3. 处理<code>&lt;resultMap&gt;</code>标签</h4>
<p>有关系型数据库使用经验的同学应该知道，select 语句执行得到的结果集实际上是一张二维表，而 Java 是一门面向对象的程序设计语言，在使用 JDBC 的时候，我们需要手动写代码将select 语句的结果集转换成 Java 对象，这是一项重复性很大的操作。</p>
<p><strong>为了将 Java 开发者从这种重复性的工作中解脱出来，MyBatis 提供了 <resultMap> 标签来定义结果集与 Java 对象之间的映射规则。</strong></p>
<p>首先，<code>&lt;resultMap&gt;</code> 标签下的每一个子标签，例如，<code>&lt;column&gt;</code>、<code>&lt;id&gt;</code> 等，都被解析一个 ResultMapping 对象，其中维护了数据库表中一个列与对应 Java 类中一个属性之间的映射关系。</p>
<p>下面是 ResultMapping 中核心字段的含义。</p>
<ul>
<li>column（String 类型）：当前标签中指定的 column 属性值，指向的是数据库表中的一个列名（或是别名）。</li>
<li>property（String 类型）：当前标签中指定的 property 属性值，指向的是与 column 列对应的属性名称。</li>
<li>javaType（Class&lt;?&gt; 类型）、jdbcType（JdbcType 类型）：当前标签指定的 javaType 属性值和 jdbcType 属性值，指定了 property 字段的 Java 类型以及对应列的 JDBC 类型。</li>
<li>typeHandler（TypeHandler&lt;?&gt; 类型）：当前标签的 typeHandler 属性值，这里指定的 TypeHandler 会覆盖默认的类型处理器。</li>
<li>nestedResultMapId（String类型）：当前标签的 resultMap 属性值，通过该属性我们可以引用另一个 <code>&lt;resultMap&gt;</code> 标签的id，然后由这个被引用的<code>&lt;resultMap&gt;</code> 标签映射结果集中的一部分列。这样，我们就可以将一个查询结果集映射成多个对象，同时确定这些对象之间的关联关系。</li>
<li>nestedQueryId（String 类型）：当前标签的select 属性，我们可以通过该属性引用另一个 <code>&lt;select&gt;</code> 标签中的select 语句定义，它会将当前列的值作为参数传入这个 select 语句。由于当前结果集可能查询出多行数据，那么可能就会导致 select 属性指定的 SQL 语句会执行多次，也就是著名的 N+1 问题。</li>
<li>columnPrefix（String 类型）：当前标签的 columnPrefix 属性值，记录了表中列名的公共前缀。</li>
<li>resultSet（String 类型）：当前标签的 resultSet 属性值。</li>
<li>lazy（boolean 类型）：当前标签的fetchType 属性，表示是否延迟加载当前标签对应的列。</li>
</ul>
<p>介绍完 ResultMapping 对象（即<code>&lt;resultMap&gt;</code> 标签下各个子标签的解析结果）之后，我们再来看<code>&lt;resultMap&gt;</code> 标签如何被解析。整个 <code>&lt;resultMap&gt;</code> 标签最终会被解析成 ResultMap 对象，它与 ResultMapping 之间的映射关系如下图所示：</p>
<p><img src="assets/CioPOWA7kqSASvnUAAPk5cQ7q3c025.png" alt="图片1.png" /></p>
<p>ResultMap 结构图</p>
<p>通过上图我们可以看出，ResultMap 中有四个集合与 ResultMapping 紧密相连。</p>
<ul>
<li>resultMappings 集合，维护了整个<code>&lt;resultMap&gt;</code> 标签解析之后得到的全部映射关系，也就是全部 ResultMapping 对象。</li>
<li>idResultMappings 集合，维护了与唯一标识相关的映射，例如，<code>&lt;id&gt;</code> 标签、<code>&lt;constructor&gt;</code> 标签下的 <code>&lt;idArg&gt;</code> 子标签解析得到的 ResultMapping 对象。如果没有定义 <code>&lt;id&gt;</code> 等唯一性标签，则由 resultMappings 集合中全部映射关系来确定一条记录的唯一性，即 idResultMappings 集合与 resulMappings 集合相同。</li>
<li>constructorResultMappings 集合，维护了 <code>&lt;constructor&gt;</code> 标签下全部子标签定义的映射关系。</li>
<li>propertyResultMappings 集合，维护了不带 Constructor 标志的映射关系。</li>
</ul>
<p>除了上述四个 ResultMapping 集合，ResultMap 中还维护了下列核心字段。</p>
<ul>
<li>id（String 类型）：当前 <code>&lt;resultMap&gt;</code> 标签的 id 属性值。</li>
<li>type（Class 类型）：当前 <code>&lt;resultMap&gt;</code> 的 type 属性值。</li>
<li>mappedColumns（Set<code>&lt;String&gt;</code> 类型）：维护了所有映射关系中涉及的 column 属性值，也就是所有的列名（或别名）。</li>
<li>hasNestedResultMaps（boolean 类型）：当前 <code>&lt;resultMap&gt;</code> 标签是否嵌套了其他 <code>&lt;resultMap&gt;</code> 标签，即这个映射关系中指定了 resultMap属性，且未指定 resultSet 属性。</li>
<li>hasNestedQueries（boolean 类型）：当前 <code>&lt;resultMap&gt;</code> 标签是否含有嵌套查询。也就是说，这个映射关系中是否指定了 select 属性。</li>
<li>autoMapping（Boolean 类型）：当前 ResultMap 是否开启自动映射的功能。</li>
<li>discriminator（Discriminator 类型）：对应 <code>&lt;discriminator&gt;</code> 标签。</li>
</ul>
<p>接下来我们开始深入分析 <code>&lt;resultMap&gt;</code> 标签解析的流程。XMLMapperBuilder的resultMapElements() 方法负责解析 Mapper 配置文件中的全部 <code>&lt;resultMap&gt;</code> 标签，其中会通过 resultMapElement() 方法解析单个 <code>&lt;resultMap&gt;</code> 标签。</p>
<p>下面是 resultMapElement() 方法解析 <code>&lt;resultMap&gt; </code>标签的核心流程。</p>
<ul>
<li>获取 <code>&lt;resultMap&gt;</code> 标签的type 属性值，这个值表示结果集将被映射成 type 指定类型的对象。如果没有指定 type 属性的话，会找其他属性值，优先级依次是：type、ofType、resultType、javaType。在这一步中会确定映射得到的对象类型，这里支持别名转换。</li>
<li>解析<code>&lt;resultMap&gt;</code>标签下的各个子标签，每个子标签都会生成一个ResultMapping 对象，这个 ResultMapping 对象会被添加到resultMappings 集合（List<code>&lt;ResultMapping&gt;</code> 类型）中暂存。这里会涉及 <code>&lt;id&gt;</code>、<code>&lt;result&gt;</code>、<code>&lt;association&gt;</code>、<code>&lt;collection&gt;</code>、<code>&lt;discriminator&gt;</code> 等子标签的解析。</li>
<li>获取 <code>&lt;resultMap&gt;</code> 标签的id 属性，默认值会拼装所有父标签的id、value 或 property 属性值。</li>
<li>获取 <code>&lt;resultMap&gt;</code> 标签的extends、autoMapping 等属性。</li>
<li>创建 ResultMapResolver 对象，ResultMapResolver 会根据上面解析到的ResultMappings 集合以及 <code>&lt;resultMap&gt;</code> 标签的属性构造 ResultMap 对象，并将其添加到 Configuration.resultMaps 集合（StrictMap 类型）中。</li>
</ul>
<h5>（1）解析 <code>&lt;id&gt;</code>、<code>&lt;result&gt;</code>、<code>&lt;constructor&gt;</code>标签</h5>
<p>在 resultMapElement() 方法中获取到 id 属性和 type 属性值之后，会调用 buildResultMappingFromContext() 方法解析上述标签得到 ResultMapping 对象，其核心逻辑如下：</p>
<ul>
<li>获取当前标签的property的属性值作为目标属性名称（如果 <code>&lt;constructor&gt;</code> 标签使用的是 name 属性）；</li>
<li>获取 column、javaType、typeHandler、jdbcType、select 等一系列属性，与获取 property 属性的方式类似；</li>
<li>根据上面解析到的信息，调用 MapperBuilderAssistant.buildResultMapping() 方法创建 ResultMapping 对象。</li>
</ul>
<p>正如 resultMapElement() 方法核心步骤描述的那样，经过解析得到 ResultMapping 对象集合之后，会记录到resultMappings 这个临时集合中，然后由 ResultMapResolver 调用 MapperBuilderAssistant.addResultMap() 方法创建 ResultMap 对象，将resultMappings 集合中的全部 ResultMapping 对象添加到其中，然后将ResultMap 对象记录到 Configuration.resultMaps 集合中。</p>
<p>下面是 MapperBuilderAssistant.addResultMap() 的具体实现：</p>
<pre><code>public ResultMap addResultMap(

        String id,

        Class&lt;?&gt; type,

        String extend,

        Discriminator discriminator,

        List&lt;ResultMapping&gt; resultMappings,

        Boolean autoMapping) {

    // ResultMap的完整id是&quot;namespace.id&quot;的格式

    id = applyCurrentNamespace(id, false);

    // 获取被继承的ResultMap的完整id，也就是父ResultMap对象的完整id

    extend = applyCurrentNamespace(extend, true);

    if (extend != null) {  // 针对extend属性的处理

        // 检测Configuration.resultMaps集合中是否存在被继承的ResultMap对象

        if (!configuration.hasResultMap(extend)) {

            throw new IncompleteElementException(&quot;Could not find a parent resultmap with id '&quot; + extend + &quot;'&quot;);

        }

        // 获取需要被继承的ResultMap对象，也就是父ResultMap对象

        ResultMap resultMap = configuration.getResultMap(extend);

        // 获取父ResultMap对象中记录的ResultMapping集合

        List&lt;ResultMapping&gt; extendedResultMappings = new ArrayList&lt;&gt;(resultMap.getResultMappings());

        // 删除需要覆盖的ResultMapping集合

        extendedResultMappings.removeAll(resultMappings);

        // 如果当前&lt;resultMap&gt;标签中定义了&lt;constructor&gt;标签，则不需要使用父ResultMap中记录

        // 的相应&lt;constructor&gt;标签，这里会将其对应的ResultMapping对象删除

        boolean declaresConstructor = false;

        for (ResultMapping resultMapping : resultMappings) {

            if (resultMapping.getFlags().contains(ResultFlag.CONSTRUCTOR)) {

                declaresConstructor = true;

                break;

            }

        }

        if (declaresConstructor) {

            extendedResultMappings.removeIf(resultMapping -&gt; resultMapping.getFlags().contains(ResultFlag.CONSTRUCTOR));

        }

        // 添加需要被继承下来的ResultMapping对象记录到resultMappings集合中

        resultMappings.addAll(extendedResultMappings);

    }

    // 创建ResultMap对象，并添加到Configuration.resultMaps集合中保存

    ResultMap resultMap = new ResultMap.Builder(configuration, id, type, resultMappings, autoMapping)

            .discriminator(discriminator)

            .build();

    configuration.addResultMap(resultMap);

    return resultMap;

}
</code></pre>
<p>至于 <code>&lt;constructor&gt; </code>标签的流程，是由XMLMapperBuilder 中的processConstructorElement() 方法实现，其中会先获取 <code>&lt;constructor&gt;</code> 标签的全部子标签，然后为每个标签添加 CONSTRUCTOR 标志（为每个<code>&lt;idArg&gt;</code> 标签添加额外的ID标志），最后通过 buildResultMappingFromContext()方法创建 ResultMapping对象并记录到 resultMappings 集合中暂存，这些 ResultMapping 对象最终也会添加到前面介绍的ResultMap 对象。</p>
<h5>（2）解析 <code>&lt;association&gt;</code> 和 <code>&lt;collection&gt;</code>标签</h5>
<p>接下来，我们来介绍解析 <code>&lt;association&gt;</code> 和 <code>&lt;collection&gt;</code>标签的核心流程，两者解析的过程基本一致。前面介绍的 buildResultMappingFromContext() 方法不仅完成了 <code>&lt;id&gt;</code>、<code>&lt;result&gt;</code> 等标签的解析，还完成了 <code>&lt;association&gt;</code> 和 <code>&lt;collection&gt;</code> 标签的解析，其中相关的代码片段如下：</p>
<pre><code>private ResultMapping buildResultMappingFromContext(XNode context, Class&lt;?&gt; resultType, List&lt;ResultFlag&gt; flags) {

    ... // &lt;association&gt;标签中其他属性的解析与&lt;result&gt;、&lt;id&gt;标签类似，这里不再展开

    // 如果&lt;association&gt;标签没有指定resultMap属性，那么就是匿名嵌套映射，需要通过

    //  processNestedResultMappings()方法解析该匿名的嵌套映射

    String nestedResultMap = context.getStringAttribute(&quot;resultMap&quot;, () -&gt;

            processNestedResultMappings(context, Collections.emptyList(), resultType));

    ... // &lt;association&gt;标签中其他属性的解析与&lt;result&gt;、&lt;id&gt;标签类似，这里不再展开

    // 根据上面解析到的属性值，创建ResultMapping对象

    return builderAssistant.buildResultMapping(resultType, property, column, javaTypeClass, jdbcTypeEnum, nestedSelect, nestedResultMap, notNullColumn, columnPrefix, typeHandlerClass, flags, resultSet, foreignColumn, lazy);

}
</code></pre>
<p>这里的 processNestedResultMappings() 方法会递归执行resultMapElement() 方法解析 <code>&lt;association&gt;</code> 标签和 <code>&lt;collection&gt;</code> 标签指定的匿名嵌套映射，得到一个完整的ResultMap 对象，并添加到Configuration.resultMaps集合中。</p>
<h5>（3）解析 <code>&lt;discriminator&gt;</code> 标签</h5>
<p>最后一个要介绍的是 <code>&lt;discriminator&gt;</code> 标签的解析过程，我们将 <code>&lt;discriminator&gt;</code> 标签与 <code>&lt;case&gt;</code> 标签配合使用，根据结果集中某列的值改变映射行为。从 resultMapElement() 方法的逻辑我们可以看出，<code>&lt;discriminator&gt;</code> 标签是由 processDiscriminatorElement() 方法专门进行解析的，具体实现如下：</p>
<pre><code>private Discriminator processDiscriminatorElement(XNode context, Class&lt;?&gt; resultType, List&lt;ResultMapping&gt; resultMappings) {

    // 从&lt;discriminator&gt;标签中解析column、javaType、jdbcType、typeHandler四个属性的逻辑非常简单，这里将这部分代码省略

    Map&lt;String, String&gt; discriminatorMap = new HashMap&lt;&gt;();

    // 解析&lt;discriminator&gt;标签的&lt;case&gt;子标签

    for (XNode caseChild : context.getChildren()) {

        String value = caseChild.getStringAttribute(&quot;value&quot;);

        // 通过前面介绍的processNestedResultMappings()方法，解析&lt;case&gt;标签，

        // 创建相应的嵌套ResultMap对象

        String resultMap = caseChild.getStringAttribute(&quot;resultMap&quot;,

                processNestedResultMappings(caseChild, resultMappings, resultType));

        // 记录该列值与对应选择的ResultMap的Id

        discriminatorMap.put(value, resultMap);

    }

    // 创建Discriminator对象

    return builderAssistant.buildDiscriminator(resultType, column, javaTypeClass, jdbcTypeEnum, typeHandlerClass, discriminatorMap);

}
</code></pre>
<h3>SQL 语句解析全流程</h3>
<p>在 Mapper.xml 映射文件中，除了上面介绍的标签之外，还有一类比较重要的标签，那就是 <code>&lt;select&gt;</code>、<code>&lt;insert&gt;</code>、<code>&lt;delete&gt;</code>、<code>&lt;update&gt;</code> 等 SQL 语句标签。虽然定义在 Mapper.xml 映射文件中，但是<strong>这些标签是由 XMLStatementBuilder 进行解析的</strong>，而不再由 XMLMapperBuilder 来完成解析。</p>
<p>在开始介绍 XMLStatementBuilder 解析 SQL 语句标签的具体实现之前，我们先来了解一下 MyBatis 在内存中是如何表示这些 SQL 语句标签的。在内存中，MyBatis 使用 SqlSource 接口来表示解析之后的 SQL 语句，其中的 SQL 语句只是一个中间态，可能包含动态 SQL 标签或占位符等信息，无法直接使用。SqlSource 接口的定义如下：</p>
<pre><code>public interface SqlSource {

    // 根据Mapper文件或注解描述的SQL语句，以及传入的实参，返回可执行的SQL

    BoundSql getBoundSql(Object parameterObject);

}
</code></pre>
<p>MyBatis 在内存中使用 MappedStatement 对象表示上述 SQL 标签。在 MappedStatement 中的 sqlSource 字段记录了 SQL 标签中定义的 SQL 语句，sqlCommandType 字段记录了 SQL 语句的类型（INSERT、UPDATE、DELETE、SELECT 或 FLUSH 类型）。</p>
<p>介绍完表示 SQL 标签的基础类之后，我们来分析 XMLStatementBuilder 解析 SQL 标签的入口方法—— parseStatementNode() 方法，在该方法中首先会根据 id 属性和 databaseId 属性决定加载匹配的 SQL 标签，然后解析其中的<code>&lt;include&gt;</code> 标签和 <code>&lt;selectKey&gt;</code> 标签，相关的代码片段如下：</p>
<pre><code>public void parseStatementNode() {

    // 获取SQL标签的id以及databaseId属性

    String id = context.getStringAttribute(&quot;id&quot;);

    String databaseId = context.getStringAttribute(&quot;databaseId&quot;);

    // 若databaseId属性值与当前使用的数据库不匹配，则不加载该SQL标签

    // 若存在相同id且databaseId不为空的SQL标签，则不再加载该SQL标签

    if (!databaseIdMatchesCurrent(id, databaseId, this.requiredDatabaseId)) {

        return;

    }

    // 根据SQL标签的名称决定其SqlCommandType

    String nodeName = context.getNode().getNodeName();

    SqlCommandType sqlCommandType = SqlCommandType.valueOf(nodeName.toUpperCase(Locale.ENGLISH));

    // 获取SQL标签的属性值，例如，fetchSize、timeout、parameterType、parameterMap、

    // resultMap、resultType、lang、resultSetType、flushCache、useCache等。

    // 这些属性的具体含义在MyBatis官方文档中已经有比较详细的介绍了，这里不再赘述

    ... ...

    // 在解析SQL语句之前，先处理其中的&lt;include&gt;标签

    XMLIncludeTransformer includeParser = new XMLIncludeTransformer(configuration, builderAssistant);

    includeParser.applyIncludes(context.getNode());

    // 获取SQL标签的parameterType、lang两个属性

    ... ...

    // 解析&lt;selectKey&gt;标签

    processSelectKeyNodes(id, parameterTypeClass, langDriver);

    // 暂时省略后面的逻辑

    ...

}
</code></pre>
<h4>1. 处理 <code>&lt;include&gt;</code> 标签</h4>
<p>在实际应用中，我们会在<code>&lt;sql&gt;</code> 标签中定义一些能够被重用的SQL 片段，在 XMLMapperBuilder.sqlElement() 方法中会根据当前使用的 DatabaseId 匹配 <code>&lt;sql&gt;</code> 标签，只有匹配的 SQL 片段才会被加载到内存。</p>
<p>在解析 SQL 标签之前，MyBatis 会先将 <code>&lt;include&gt;</code> 标签转换成对应的 SQL 片段（即定义在 <code>&lt;sql&gt;</code> 标签内的文本），这个转换过程是在 XMLIncludeTransformer.applyIncludes() 方法中实现的（其中不仅包含了 <code>&lt;include&gt;</code> 标签的处理，还包含了“${}”占位符的处理）。</p>
<p>针对 <code>&lt;include&gt;</code> 标签的处理如下：</p>
<ul>
<li>查找 refid 属性指向的 <code>&lt;sql&gt;</code> 标签，得到其对应的 Node 对象；</li>
<li>解析 <code>&lt;include&gt;</code> 标签下的 <code>&lt;property&gt;</code> 标签，将得到的键值对添加到 variablesContext 集合（Properties 类型）中，并形成新的 Properties 对象返回，用于替换占位符；</li>
<li>递归执行 applyIncludes()方法，因为在 <code>&lt;sql&gt;</code> 标签的定义中可能会使用 <code>&lt;include&gt;</code> 引用其他 SQL 片段，在 applyIncludes()方法递归的过程中，如果遇到“${}”占位符，则使用 variablesContext 集合中的键值对进行替换；</li>
<li>最后，将 <code>&lt;include&gt;</code> 标签替换成 <code>&lt;sql&gt;</code> 标签的内容。</li>
</ul>
<p>通过上面逻辑可以看出，<code>&lt;include&gt;</code> 标签和 <code>&lt;sql&gt;</code> 标签是可以嵌套多层的，此时就会涉及 applyIncludes()方法的递归，同时可以配合“${}”占位符，实现 SQL 片段模板化，更大程度地提高 SQL 片段的重用率。</p>
<h4>2. 处理 <code>&lt;selectKey&gt;</code> 标签</h4>
<p>在有的数据库表设计场景中，我们会添加一个自增 ID 字段作为主键，例如，用户 ID、订单 ID 或者这个自增 ID 本身并没有什么业务含义，只是一个唯一标识而已。在某些业务逻辑里面，我们希望在执行 insert 语句的时候返回这个自增 ID 值，<code>&lt;selectKey&gt;</code> 标签就可以实现自增 ID 的获取。<code>&lt;selectKey&gt;</code> 标签不仅可以获取自增 ID，还可以指定其他 SQL 语句，从其他表或执行数据库的函数获取字段值。</p>
<p><strong>parseSelectKeyNode() 方法是解析 <selectKey> 标签的核心所在</strong>，其中会解析 <code>&lt;selectKey&gt;</code> 标签的各个属性，并根据这些属性值将其中的 SQL 语句解析成 MappedStatement 对象，具体实现如下：</p>
<pre><code>private void parseSelectKeyNode(String id, XNode nodeToHandle, Class&lt;?&gt; parameterTypeClass, LanguageDriver langDriver, String databaseId) {

    ... // 解析&lt;selectKey&gt;标签的resultType、statementType、keyProperty等属性

    // 通过LanguageDriver解析&lt;selectKey&gt;标签中的SQL语句，得到对应的SqlSource对象

    SqlSource sqlSource = langDriver.createSqlSource(configuration, nodeToHandle, parameterTypeClass);

    SqlCommandType sqlCommandType = SqlCommandType.SELECT;

    // 创建MappedStatement对象

    builderAssistant.addMappedStatement(id, sqlSource, statementType, sqlCommandType,

            fetchSize, timeout, parameterMap, parameterTypeClass, resultMap, resultTypeClass,

            resultSetTypeEnum, flushCache, useCache, resultOrdered,

            keyGenerator, keyProperty, keyColumn, databaseId, langDriver, null);

    id = builderAssistant.applyCurrentNamespace(id, false);

    // 创建&lt;selectKey&gt;标签对应的KeyGenerator对象，这个KeyGenerator对象会添加到Configuration.keyGenerators集合中

    MappedStatement keyStatement = configuration.getMappedStatement(id, false);

    configuration.addKeyGenerator(id, new SelectKeyGenerator(keyStatement, executeBefore));

}
</code></pre>
<h4>3. 处理 SQL 语句</h4>
<p>经过 <code>&lt;include&gt;</code> 标签和 <code>&lt;selectKey&gt;</code> 标签的处理流程之后，XMLStatementBuilder 中的 parseStatementNode()方法接下来就要开始处理 SQL 语句了，相关的代码片段之前被省略了，这里我们详细分析一下：</p>
<pre><code>public void parseStatementNode() {

    // 前面是解析&lt;selectKey&gt;和&lt;include&gt;标签的逻辑，这里不再展示

    // 当执行到这里的时候，&lt;selectKey&gt;和&lt;include&gt;标签已经被解析完毕，并删除掉了

    // 下面是解析SQL语句的逻辑，也是parseStatementNode()方法的核心

    // 通过LanguageDriver.createSqlSource()方法创建SqlSource对象

    SqlSource sqlSource = langDriver.createSqlSource(configuration, context, parameterTypeClass);

    // 获取SQL标签中配置的resultSets、keyProperty、keyColumn等属性，以及前面解析&lt;selectKey&gt;标签得到的KeyGenerator对象等，

    // 这些信息将会填充到MappedStatement对象中

    // 根据上述属性信息创建MappedStatement对象，并添加到Configuration.mappedStatements集合中保存

    builderAssistant.addMappedStatement(id, sqlSource, statementType, sqlCommandType,

            fetchSize, timeout, parameterMap, parameterTypeClass, resultMap, resultTypeClass,

            resultSetTypeEnum, flushCache, useCache, resultOrdered,

            keyGenerator, keyProperty, keyColumn, databaseId, langDriver, resultSets);

}
</code></pre>
<p>这里解析 SQL 语句<strong>使用的是 LanguageDriver 接口</strong>，其核心实现是 XMLLanguageDriver，继承关系如下图所示：</p>
<p><img src="assets/Cgp9HWA7ksyAUvrwAADwoAT3J5M370.png" alt="图片2.png" /></p>
<p>LanguageDriver 继承关系图</p>
<p>在 createSqlSource() 方法中，XMLLanguageDriver 会依赖 XMLScriptBuilder 创建 SqlSource 对象，XMLScriptBuilder 首先会判断 SQL 语句是否为动态SQL，判断的核心逻辑在 parseDynamicTags()方法中，核心实现如下：</p>
<pre><code>protected MixedSqlNode parseDynamicTags(XNode node) {

    List&lt;SqlNode&gt; contents = new ArrayList&lt;&gt;(); // 解析后的SqlNode结果集合

    NodeList children = node.getNode().getChildNodes();

    // 获取SQL标签下的所有节点，包括标签节点和文本节点

    for (int i = 0; i &lt; children.getLength(); i++) {

        XNode child = node.newXNode(children.item(i));

        if (child.getNode().getNodeType() == Node.CDATA_SECTION_NODE ||

                child.getNode().getNodeType() == Node.TEXT_NODE) {

            // 处理文本节点，也就是SQL语句

            String data = child.getStringBody(&quot;&quot;);

            TextSqlNode textSqlNode = new TextSqlNode(data);

            // 解析SQL语句，如果含有未解析的&quot;${}&quot;占位符，则为动态SQL

            if (textSqlNode.isDynamic()) {

                contents.add(textSqlNode);

                isDynamic = true; // 标记为动态SQL语句

            } else {

                contents.add(new StaticTextSqlNode(data));

            }

        } else if (child.getNode().getNodeType() == Node.ELEMENT_NODE) {

            // 如果解析到一个子标签，那么一定是动态SQL

            // 这里会根据不同的标签，获取不同的NodeHandler，然后由NodeHandler进行后续解析

            String nodeName = child.getNode().getNodeName();

            NodeHandler handler = nodeHandlerMap.get(nodeName);

            if (handler == null) {

                throw new BuilderException(&quot;Unknown element &lt;&quot; + nodeName + &quot;&gt; in SQL statement.&quot;);

            }

            // 处理动态SQL语句，并将解析得到的SqlNode对象记录到contents集合中

            handler.handleNode(child, contents);

            isDynamic = true;

        }

    }

    // 解析后的SqlNode集合将会被封装成MixedSqlNode返回

    return new MixedSqlNode(contents);

}
</code></pre>
<p>这里使用 SqlNode 接口来表示一条 SQL 语句的不同部分，其中，TextSqlNode 表示的是SQL 语句的文本（可能包含“${}”占位符），StaticTextSqlNode 表示的是不包含占位符的SQL 语句文本。</p>
<p>另外一个新接口是NodeHandler，它有很多实现类，如下图所示：</p>
<p><img src="assets/Cgp9HWA7kvSAHP1yAAEyhRwHGEE543.png" alt="图片3.png" /></p>
<p>NodeHandler 继承关系图</p>
<p><strong>NodeHandler接口负责解析动态 SQL 内的标签</strong>，生成相应的 SqlNode 对象，通过 NodeHandler 实现类的名称，我们就可以大概猜测到其解析的标签名称。以 IfHandler 为例，它解析的就是 <code>&lt;if&gt;</code> 标签，其核心实现如下：</p>
<pre><code>private class IfHandler implements NodeHandler {

    public void handleNode(XNode nodeToHandle, List&lt;SqlNode&gt; targetContents) {

        // 通过parseDynamicTags()方法，解析&lt;if&gt;标签下嵌套的动态SQL

        MixedSqlNode mixedSqlNode = parseDynamicTags(nodeToHandle);

        // 获取&lt;if&gt;标签判断分支的条件

        String test = nodeToHandle.getStringAttribute(&quot;test&quot;);

        // 创建IfNode对象(也是SqlNode接口的实现)，并将其保存下来

        IfSqlNode ifSqlNode = new IfSqlNode(mixedSqlNode, test);

        targetContents.add(ifSqlNode);

    }

}
</code></pre>
<p>完成了对 SQL 语句的解析，得到了相应的 MixedSqlNode对象之后，XMLScriptBuilder 会根据 SQL 语句的类型生成不同的 SqlSource 实现：</p>
<pre><code>public SqlSource parseScriptNode() {

    // 对SQL语句进行解析

    MixedSqlNode rootSqlNode = parseDynamicTags(context);

    SqlSource sqlSource;

    if (isDynamic) { // 根据该SQL是否为动态SQL，创建不同的SqlSource实现

        sqlSource = new DynamicSqlSource(configuration, rootSqlNode);

    } else {

        sqlSource = new RawSqlSource(configuration, rootSqlNode, parameterType);

    }

    return sqlSource;

}
</code></pre>
<h3>总结</h3>
<p>这一讲我们重点介绍了 MyBatis 在初始化过程中对 Mapper.xml 映射文件的解析。</p>
<p>首先，我们着重介绍了 Mapper.xml 映射文件中对 <code>&lt;cache&gt;</code> 标签、<code>&lt;cache-ref&gt;</code> 标签以及 <code>&lt;resultMap&gt;</code> 标签（包括它的各个子标签）的解析流程，让我们知道 MyBatis是如何正确理解二级缓存的配置信息以及我们定义的各种映射规则。</p>
<p>然后，我们详细分析了 MyBatis 对 Mapper.xml 映射文件中 SQL 语句标签的解析，其中涉及 <code>&lt;include&gt;</code>、<code>&lt;selectKey&gt;</code> 等标签的处理逻辑。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="10&#32;&#32;鸟瞰&#32;MyBatis&#32;初始化，把握&#32;MyBatis&#32;启动流程脉络（上）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="12&#32;&#32;深入分析动态&#32;SQL&#32;语句解析全流程（上）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43571f9c7a645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
