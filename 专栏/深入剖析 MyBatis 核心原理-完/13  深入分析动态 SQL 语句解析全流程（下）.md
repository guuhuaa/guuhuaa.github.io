<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>13  深入分析动态 SQL 语句解析全流程（下）.md</title>
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

                    <a class="current-tab" href="13&#32;&#32;深入分析动态&#32;SQL&#32;语句解析全流程（下）.md">13  深入分析动态 SQL 语句解析全流程（下）.md</a>
                    

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
                        <div><h1>13  深入分析动态 SQL 语句解析全流程（下）</h1>
<p>在上一讲，我们讲解了 MyBatis 中动态 SQL 语句的相关内容，重点介绍了 MyBatis 使用到的 OGNL 表达式、组合模式、DynamicContext 上下文以及多个动态 SQL 标签对应的 SqlNode 实现。今天我们就紧接着上一讲，继续介绍剩余 SqlNode 实现以及 SqlSource 的相关内容。</p>
<h3>SqlNode 剩余实现类</h3>
<p>在上一讲我们已经介绍了 StaticTextSqlNode、MixedSqlNode、TextSqlNode、IfSqlNode、TrimSqlNode 这几个 SqlNode 的实现，下面我们再把剩下的三个 SqlNode 实现类也说明下。</p>
<h4>1. ForeachSqlNode</h4>
<p>在动态 SQL 语句中，我们可以<strong>使用 <foreach> 标签对一个集合进行迭代</strong>。在迭代过程中，我们可以通过 index 属性值指定的变量作为元素的下标索引（迭代 Map 集合的话，就是 Key 值），使用 item 属性值指定的变量作为集合元素（迭代 Map 集合的话，就是 Value 值）。另外，我们还可以通过 open 和 close 属性在迭代开始前和结束后添加相应的字符串，也允许使用 separator 属性自定义分隔符。这里要介绍的 ForeachSqlNode 就是 <code>&lt;foreach&gt;</code> 标签的抽象。</p>
<p>下面我们就来分析一下 ForeachSqlNode 的 apply() 方法是如何实现循环的。</p>
<p>首先，向 DynamicContext.sqlBuilder 中追加 open 属性值指定的字符串，然后通过 ExpressionEvaluator 工具类解析 <code>&lt;foreach&gt;</code> 标签中 collection 属性指定的表达式，得到一个集合对象，并遍历这个集合。</p>
<p>接下来，为每个元素创建一个 PrefixedContext 对象。PrefixedContext 是 DynamicContext 的一个装饰器，其中记录了一个 prefix 前缀信息（其实就是 <code>&lt;foreach&gt;</code> 标签中的 separator 属性值），在其 apply() 方法中会先追加 prefix 前缀（迭代第一个元素的时候，prefix 为空字符串），然后追加 SQL 片段。</p>
<p>如果传入的集合是 Map 类型，则通过 applyIndex() 方法和 applyItem() 方法将 Map 中的 Key 和 Value 记录到 PrefixedContext 中，示例如下：</p>
<pre><code>private void applyIndex(DynamicContext context, Object o, int i) {

    if (index != null) {

        // Key值与index属性值指定的变量名称绑定

        context.bind(index, o); 

        // Key值还会与&quot;__frch_&quot;+index属性值+ &quot;_&quot; + i 这个变量绑定

        // 这里传入的 i 是一个自增序列，由底层的 DynamicContext 统一维护。

        context.bind(itemizeItem(index, i), o);

    }

}

private void applyItem(DynamicContext context, Object o, int i) {

    if (item != null) {

        // Value值与item属性值指定的变量名称绑定

        context.bind(item, o);

        // Value值还会与&quot;__frch_&quot;+item属性值+ &quot;_&quot; + i 这个变量绑定

        context.bind(itemizeItem(item, i), o);

    }

}
</code></pre>
<p>但如果传入的集合不是 Map 类型，则通过 applyIndex() 方法和 applyItem() 方法将集合元素的下标索引和元素值本身绑定到 PrefixedContext 中。</p>
<p>完成 PrefixedContext 的绑定之后，会调用 <code>&lt;foreach&gt;</code> 标签下子 SqlNode 的 apply() 方法，其中传入的 DynamicContext 实际上是 ForEachSqlNode$FilteredDynamicContext 这个内部类，它也是 DynamicContext 的装饰器，核心功能是：根据前面在 PrefixedContext 中绑定的各种变量，处理 SQL 片段中的“#{}”占位符。FilteredDynamicContext 在多次循环中的处理效果如下图所示：</p>
<p><img src="assets/Cgp9HWBB-4WADZbeAAIPDjI-G2A404.png" alt="Drawing 1.png" /></p>
<p>FilteredDynamicContext 变化过程示意图</p>
<p>下面是 FilteredDynamicContext.appendSql() 方法的核心实现：</p>
<pre><code>public void appendSql(String sql) {

    // 创建识别&quot;#{}&quot;的GenericTokenParser解析器

    GenericTokenParser parser = new GenericTokenParser(&quot;#{&quot;, &quot;}&quot;, content -&gt; {

        // 这个TokenHandler实现会将#{i}替换成#{__frch_i_0}、#{__frch_i_1}...

        String newContent = content.replaceFirst(&quot;^\\s*&quot; + item + &quot;(?![^.,:\\s])&quot;, itemizeItem(item, index));

        if (itemIndex != null &amp;&amp; newContent.equals(content)) {

            // 这里会将#{j}替换成#{__frch_j_0}、#{__frch_j_1}...

            newContent = content.replaceFirst(&quot;^\\s*&quot; + itemIndex + &quot;(?![^.,:\\s])&quot;, itemizeItem(itemIndex, index));

        }

        return &quot;#{&quot; + newContent + &quot;}&quot;;

    });

    // 保存解析后的SQL片段

    delegate.appendSql(parser.parse(sql));

}
</code></pre>
<p>完成集合中全部元素的迭代处理之后，ForeachSqlNode.apply() 方法还会调用 applyClose() 方法追加 close 属性指定的后缀。最后，从 DynamicContext 上下文中删除 index 属性值和 item 属性值指定的变量。</p>
<h4>2. ChooseSqlNode</h4>
<p>在有的业务场景中，可能会碰到非常多的分支判断，在 Java 中，我们可以通过 switch...case...default 的方式来编写这段代码；在 MyBatis 的动态 SQL 语句中，我们可以使用 <code>&lt;choose&gt;</code>、<code>&lt;when&gt;</code> 和 <code>&lt;otherwise&gt;</code> 三个标签来实现类似的效果。</p>
<p><strong><choose> 标签会被 MyBatis 解析成 ChooseSqlNode 对象，<when> 标签会被解析成 IfSqlNode 对象，<otherwise> 标签会被解析成 MixedSqlNode 对象。</strong></p>
<p>IfSqlNode 和 MixedSqlNode 的核心实现在上一讲中我们已经分析过了，这里不再重复。ChooseSqlNode 的实现也比较简单，其中维护了一个 List<code>&lt;SqlNode&gt;</code> 集合（ifSqlNodes 字段）用来记录所有 <code>&lt;when&gt;</code> 子标签对应的 IfSqlNode 对象，同时还维护了一个 SqlNode 类型字段（defaultSqlNode 字段）用来记录 <code>&lt;otherwise&gt;</code> 子标签生成的 MixedSqlNode 对象，该字段可以为 null。</p>
<p>在 ChooseSqlNode 的 apply() 方法中，首先会尝试迭代全部 IfSqlNode 节点并执行 apply() 方法，我们知道任意一个 IfSqlNode.apply() 方法返回 true，即表示命中该分支，此时整个 ChooseSqlNode.apply() 返回 true，否则尝试执行 defaultSqlNode.apply() 方法并返回 true，即进入默认分支。如果 defaultSqlNode 字段为 null，则返回 false。</p>
<h4>3. VarDeclSqlNode</h4>
<p>VarDeclSqlNode 抽象了 <code>&lt;bind&gt;</code> 标签，其<strong>核心功能是将一个 OGNL 表达式的值绑定到一个指定的变量名上，并记录到 DynamicContext 上下文中</strong>。</p>
<p>VarDeclSqlNode 中的 name 字段维护了 <code>&lt;bind&gt;</code> 标签中 name 属性的值，expression 字段记录了 <code>&lt;bind&gt;</code> 标签中 value 属性的值（一般是一个 OGNL 表达式）。</p>
<p>在 apply() 方法中，VarDeclSqlNode 首先会通过 OGNL 工具类解析 expression 这个表达式的值，然后将解析结果与 name 字段的值一起绑定到 DynamicContext 上下文中，这样后面就可以通过 name 字段值获取这个表达式的值了。</p>
<h3>SqlSourceBuilder</h3>
<p>动态 SQL 语句经过上述 SqlNode 的解析之后，接着会由 SqlSourceBuilder 进行下一步处理。</p>
<p>SqlSourceBuilder 的核心操作主要有两个：</p>
<ul>
<li><strong>解析“#{}”占位符中携带的各种属性</strong>，例如，“#{id, javaType=int, jdbcType=NUMERIC, typeHandler=MyTypeHandler}”这个占位符，指定了 javaType、jdbcType、typeHandler 等配置；</li>
<li><strong>将 SQL 语句中的“#{}”占位符替换成“?”占位符</strong>，替换之后的 SQL 语句就可以提交给数据库进行编译了。</li>
</ul>
<p>SqlSourceBuilder 的入口是 parse() 方法，这里首先会创建一个识别“#{}”占位符的 GenericTokenParser 解析器，当识别到“#{}”占位符的时候，就<strong>由 ParameterMappingTokenHandler 这个 TokenHandler 实现完成上述两个核心步骤</strong>。</p>
<p>ParameterMappingTokenHandler 中维护了一个 List<code>&lt;ParameterMapping&gt;</code> 类型的集合（parameterMappings 字段），用来记录每个占位符参数解析后的结果，ParameterMapping 记录了占位符名称（property 字段）、jdbcType 属性值（jdbcType 字段）、javaType 属性值（javaType 字段）、typeHandler 属性值（typeHandler 字段）等。</p>
<p>在 buildParameterMapping() 方法中会通过 ParameterExpression 工具类解析“#{}”占位符，然后通过 ParameterMapping.Builder 创建对应的 ParameterMapping 对象。这里得到的 ParameterMapping 就会被记录到 parameterMappings 集合中。</p>
<p>ParameterMappingTokenHandler.handleToken() 方法的核心逻辑如下：</p>
<pre><code>public String handleToken(String content) {

    // content是前面通过GenericTokenParser识别到的#{}占位符，

    // 这里通过buildParameterMapping()方法进行解析，得到ParameterMapping对象

    parameterMappings.add(buildParameterMapping(content));

    // 直接返回&quot;?&quot;占位符，替换原有的#{}占位符

    return &quot;?&quot;;

}
</code></pre>
<p>SqlSourceBuilder 完成了“#{}”占位符的解析和替换之后，会将最终的 SQL 语句以及得到的 ParameterMapping 集合封装成一个 StaticSqlSource 对象并返回。</p>
<h3>SqlSource</h3>
<p>经过上述一系列处理之后，SQL 语句最终会由 SqlSource 进行最后的处理。</p>
<p><strong>在 SqlSource 接口中只定义了一个 getBoundSql() 方法，它控制着动态 SQL 语句解析的整个流程</strong>，它会根据从 Mapper.xml 映射文件（或注解）解析到的 SQL 语句以及执行 SQL 时传入的实参，返回一条可执行的 SQL。</p>
<p>下图展示了 SqlSource 接口的核心实现：</p>
<p><img src="assets/CioPOWBB-6CAFZlRAAEeTrexVm4358.png" alt="Drawing 3.png" /></p>
<p>SqlSource 接口继承图</p>
<p>下面我们简单介绍一下这三个核心实现类的具体含义。</p>
<ul>
<li>DynamicSqlSource：当 SQL 语句中包含动态 SQL 的时候，会使用 DynamicSqlSource 对象。</li>
<li>RawSqlSource：当 SQL 语句中只包含静态 SQL 的时候，会使用 RawSqlSource 对象。</li>
<li>StaticSqlSource：DynamicSqlSource 和 RawSqlSource 经过一系列解析之后，会得到最终可提交到数据库的 SQL 语句，这个时候就可以通过 StaticSqlSource 进行封装了。</li>
</ul>
<h4>1. DynamicSqlSource</h4>
<p>DynamicSqlSource 作为最常用的 SqlSource 实现，<strong>主要负责解析动态 SQL 语句</strong>。</p>
<p>DynamicSqlSource 中维护了一个 SqlNode 类型的字段（rootSqlNode 字段），用于记录整个 SqlNode 树形结构的根节点。在 DynamicSqlSource 的 getBoundSql() 方法实现中，会使用前面介绍的 SqlNode、SqlSourceBuilder 等组件，完成动态 SQL 语句以及“#{}”占位符的解析，具体的实现如下：</p>
<pre><code>public BoundSql getBoundSql(Object parameterObject) {

    // 创建DynamicContext对象，parameterObject是用户传入的实参

    DynamicContext context = new DynamicContext(configuration, parameterObject);

    // 调用rootSqlNode.apply()方法，完成整个树形结构中全部SqlNode对象对SQL片段的解析

    // 这里无须关心rootSqlNode这棵树中到底有多少SqlNode对象，每个SqlNode对象的行为都是一致的，

    // 都会将解析之后的SQL语句片段追加到DynamicContext中，形成最终的、完整的SQL语句

    // 这是使用组合设计模式的好处

    rootSqlNode.apply(context);

    // 通过SqlSourceBuilder解析&quot;#{}&quot;占位符中的属性，并将SQL语句中的&quot;#{}&quot;占位符替换成&quot;?&quot;占位符

    SqlSourceBuilder sqlSourceParser = new SqlSourceBuilder(configuration);

    Class&lt;?&gt; parameterType = parameterObject == null ? Object.class : parameterObject.getClass();

    SqlSource sqlSource = sqlSourceParser.parse(context.getSql(), parameterType, context.getBindings());

    // 创建BoundSql对象

    BoundSql boundSql = sqlSource.getBoundSql(parameterObject);

    context.getBindings().forEach(boundSql::setAdditionalParameter);

    return boundSql;

}
</code></pre>
<p>这里最终返回的 BoundSql 对象，包含了解析之后的 SQL 语句（sql 字段）、每个“#{}”占位符的属性信息（parameterMappings 字段 ，List<code>&lt;ParameterMapping&gt;</code> 类型）、实参信息（parameterObject 字段）以及 DynamicContext 中记录的 KV 信息（additionalParameters 集合，Map<code>&lt;String, Object&gt;</code> 类型）。</p>
<p>后面在讲解 StatementHandler、Executor 如何执行 SQL 语句的时候，我们还会继续介绍 BoundSql 的相关内容，到时候你可以跟这里联系起来学习。</p>
<h4>2. RawSqlSource</h4>
<p>接下来我们看 SqlSource 的第二个实现—— RawSqlSource，它与 DynamicSqlSource 有两个不同之处：</p>
<ul>
<li>RawSqlSource 处理的是非动态 SQL 语句，DynamicSqlSource 处理的是动态 SQL 语句；</li>
<li>RawSqlSource 解析 SQL 语句的时机是在初始化流程中，而 DynamicSqlSource 解析动态 SQL 的时机是在程序运行过程中，也就是运行时解析。</li>
</ul>
<p>这里我们需要先来回顾一下前面介绍的 XMLScriptBuilder.parseDynamicTags() 方法，其中会<strong>判断一个 SQL 片段</strong>是否为动态 SQL，判断的标准是：<strong>如果这个 SQL 片段包含了未解析的“${}”占位符或动态 SQL 标签，则为动态 SQL 语句</strong>。但注意，如果是只包含了“#{}”占位符，也不是动态 SQL。</p>
<p>XMLScriptBuilder. parseScriptNode() 方法而 会<strong>判断整个 SQL 语句</strong>是否为动态 SQL，判断的依据是：<strong>如果 SQL 语句中包含任意一个动态 SQL 片段，那么整个 SQL 即为动态 SQL 语句</strong>。</p>
<p>总结来说，对于动态 SQL 语句，MyBatis 会创建 DynamicSqlSource 对象进行处理，而对于非动态 SQL 语句，则会创建 RawSqlSource 对象进行处理。</p>
<p>RawSqlSource 在构造方法中，会调用 SqlNode.apply() 方法将 SQL 片段组装成完整 SQL，然后通过 SqlSourceBuilder 处理“#{}”占位符，得到 StaticSqlSource 对象。这两步处理与 DynamicSqlSource 完全一样，只不过执行的时机是在 RawSqlSource 对象的初始化过程中（即 MyBatis 框架初始化流程中），而不是在 getBoundSql() 方法被调用时（即运行时）。</p>
<p>最后，RawSqlSource.getBoundSql() 方法实现是直接调用 StaticSqlSource.getBoundSql() 方法返回一个 BoundSql 对象。</p>
<p>通过前面的介绍我们知道，无论是 DynamicSqlSource 还是 RawSqlSource，底层都依赖 SqlSourceBuilder 解析之后得到的 StaticSqlSource 对象。StaticSqlSource 中维护了解析之后的 SQL 语句以及“#{}”占位符的属性信息（List<code>&lt;ParameterMapping&gt;</code> 集合），其 getBoundSql() 方法是真正创建 BoundSql 对象的地方，这个 BoundSql 对象包含了上述 StaticSqlSource 的两个字段以及实参的信息。</p>
<h3>总结</h3>
<p>我们紧接上一讲的内容，往后介绍了 SqlNode 接口剩余的实现类，其中包括 ForeachSqlNode、ChooseSqlNode 等，这些 SqlNode 实现类都对应我们常用的动态 SQL 标签。</p>
<p>接下来，我们还介绍了 SqlSourceBuilder 以及 SqlSource 接口的内容，其中针对不同类型的 SQL 语句，MyBatis 抽象出了不同的 SqlSource 实现类，也就是文中介绍的 DynamicSqlSource、RawSqlSource 以及 StaticSqlSource。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="12&#32;&#32;深入分析动态&#32;SQL&#32;语句解析全流程（上）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="14&#32;&#32;探究&#32;MyBatis&#32;结果集映射机制背后的秘密（上）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435729feba645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
