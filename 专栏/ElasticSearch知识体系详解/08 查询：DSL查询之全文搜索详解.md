<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>08 查询：DSL查询之全文搜索详解.md</title>
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

                    
                    <a href="01&#32;认知：ElasticSearch基础概念.md">01 认知：ElasticSearch基础概念.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;认知：Elastic&#32;Stack生态和场景方案.md">02 认知：Elastic Stack生态和场景方案.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;安装：ElasticSearch和Kibana安装.md">03 安装：ElasticSearch和Kibana安装.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;入门：查询和聚合的基础使用.md">04 入门：查询和聚合的基础使用.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;索引：索引管理详解.md">05 索引：索引管理详解.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;索引：索引模板(Index&#32;Template)详解.md">06 索引：索引模板(Index Template)详解.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;查询：DSL查询之复合查询详解.md">07 查询：DSL查询之复合查询详解.md</a>

                </li>
                <li>

                    <a class="current-tab" href="08&#32;查询：DSL查询之全文搜索详解.md">08 查询：DSL查询之全文搜索详解.md</a>
                    

                </li>
                <li>

                    
                    <a href="09&#32;查询：DSL查询之Term详解.md">09 查询：DSL查询之Term详解.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;聚合：聚合查询之Bucket聚合详解.md">10 聚合：聚合查询之Bucket聚合详解.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;聚合：聚合查询之Metric聚合详解.md">11 聚合：聚合查询之Metric聚合详解.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;聚合：聚合查询之Pipline聚合详解.md">12 聚合：聚合查询之Pipline聚合详解.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;原理：从图解构筑对ES原理的初步认知.md">13 原理：从图解构筑对ES原理的初步认知.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;原理：ES原理知识点补充和整体结构.md">14 原理：ES原理知识点补充和整体结构.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;原理：ES原理之索引文档流程详解.md">15 原理：ES原理之索引文档流程详解.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;原理：ES原理之读取文档流程详解.md">16 原理：ES原理之读取文档流程详解.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;优化：ElasticSearch性能优化详解.md">17 优化：ElasticSearch性能优化详解.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;大厂实践：腾讯万亿级&#32;Elasticsearch&#32;技术实践.md">18 大厂实践：腾讯万亿级 Elasticsearch 技术实践.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;资料：Awesome&#32;Elasticsearch.md">19 资料：Awesome Elasticsearch.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;WrapperQuery.md">20 WrapperQuery.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;备份和迁移.md">21 备份和迁移.md</a>

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
                        <div><h1>08 查询：DSL查询之全文搜索详解</h1>
<h2>写在前面:谈谈如何从官网学习</h2>
<p>提示</p>
<p>很多读者在看官方文档学习时存在一个误区，以DSL中full text查询为例，其实内容是非常多的， 没有取舍/没重点去阅读， 要么需要花很多时间，要么头脑一片浆糊。所以这里重点谈谈我的理解。@pdai</p>
<p>一些理解：</p>
<ul>
<li>第一点：<strong>全局观</strong>，即我们现在学习内容在整个体系的哪个位置？</li>
</ul>
<p>如下图，可以很方便的帮助你构筑这种体系</p>
<p><img src="assets/es-dsl-full-text-3.png" alt="img" /></p>
<ul>
<li>第二点： <strong>分类别</strong>，从上层理解，而不是本身</li>
</ul>
<p>比如Full text Query中，我们只需要把如下的那么多点分为3大类，你的体系能力会大大提升</p>
<p><img src="assets/es-dsl-full-text-1.png" alt="img" /></p>
<ul>
<li>第三点： <strong>知识点还是API</strong>？ API类型的是可以查询的，只需要知道大致有哪些功能就可以了。</li>
</ul>
<p><img src="assets/es-dsl-full-text-2.png" alt="img" /></p>
<h2>Match类型</h2>
<blockquote>
<p>第一类：match 类型</p>
</blockquote>
<h3>match 查询的步骤</h3>
<p>在(指定字段查询)中我们已经介绍了match查询。</p>
<ul>
<li><strong>准备一些数据</strong></li>
</ul>
<p>这里我们准备一些数据，通过实例看match 查询的步骤</p>
<pre><code class="language-bash">PUT /test-dsl-match
{ &quot;settings&quot;: { &quot;number_of_shards&quot;: 1 }} 

POST /test-dsl-match/_bulk
{ &quot;index&quot;: { &quot;_id&quot;: 1 }}
{ &quot;title&quot;: &quot;The quick brown fox&quot; }
{ &quot;index&quot;: { &quot;_id&quot;: 2 }}
{ &quot;title&quot;: &quot;The quick brown fox jumps over the lazy dog&quot; }
{ &quot;index&quot;: { &quot;_id&quot;: 3 }}
{ &quot;title&quot;: &quot;The quick brown fox jumps over the quick dog&quot; }
{ &quot;index&quot;: { &quot;_id&quot;: 4 }}
{ &quot;title&quot;: &quot;Brown fox brown dog&quot; }
</code></pre>
<ul>
<li><strong>查询数据</strong></li>
</ul>
<pre><code class="language-bash">GET /test-dsl-match/_search
{
    &quot;query&quot;: {
        &quot;match&quot;: {
            &quot;title&quot;: &quot;QUICK!&quot;
        }
    }
}
</code></pre>
<p>Elasticsearch 执行上面这个 match 查询的步骤是：</p>
<ol>
<li><strong>检查字段类型</strong> 。</li>
</ol>
<p>标题 title 字段是一个 string 类型（ analyzed ）已分析的全文字段，这意味着查询字符串本身也应该被分析。</p>
<ol>
<li><strong>分析查询字符串</strong> 。</li>
</ol>
<p>将查询的字符串 QUICK! 传入标准分析器中，输出的结果是单个项 quick 。因为只有一个单词项，所以 match 查询执行的是单个底层 term 查询。</p>
<ol>
<li><strong>查找匹配文档</strong> 。</li>
</ol>
<p>用 term 查询在倒排索引中查找 quick 然后获取一组包含该项的文档，本例的结果是文档：1、2 和 3 。</p>
<ol>
<li><strong>为每个文档评分</strong> 。</li>
</ol>
<p>用 term 查询计算每个文档相关度评分 _score ，这是种将词频（term frequency，即词 quick 在相关文档的 title 字段中出现的频率）和反向文档频率（inverse document frequency，即词 quick 在所有文档的 title 字段中出现的频率），以及字段的长度（即字段越短相关度越高）相结合的计算方式。</p>
<ul>
<li><strong>验证结果</strong></li>
</ul>
<p><img src="assets/es-dsl-full-text-4.png" alt="img" /></p>
<h3>match多个词深入</h3>
<p>我们在上文中复合查询中已经使用了match多个词，比如“Quick pets”； 这里我们通过例子带你更深入理解match多个词</p>
<ul>
<li><strong>match多个词的本质</strong></li>
</ul>
<p>查询多个词&quot;BROWN DOG!&quot;</p>
<pre><code class="language-bash">GET /test-dsl-match/_search
{
    &quot;query&quot;: {
        &quot;match&quot;: {
            &quot;title&quot;: &quot;BROWN DOG&quot;
        }
    }
}
</code></pre>
<p><img src="assets/es-dsl-full-text-5.png" alt="img" /></p>
<p>因为 match 查询必须查找两个词（ [&quot;brown&quot;,&quot;dog&quot;] ），它在内部实际上先执行两次 term 查询，然后将两次查询的结果合并作为最终结果输出。为了做到这点，它将两个 term 查询包入一个 bool 查询中，</p>
<p>所以上述查询的结果，和如下语句查询结果是等同的</p>
<pre><code class="language-bash">GET /test-dsl-match/_search
{
  &quot;query&quot;: {
    &quot;bool&quot;: {
      &quot;should&quot;: [
        {
          &quot;term&quot;: {
            &quot;title&quot;: &quot;brown&quot;
          }
        },
        {
          &quot;term&quot;: {
            &quot;title&quot;: &quot;dog&quot;
          }
        }
      ]
    }
  }
}
</code></pre>
<p><img src="assets/es-dsl-full-text-6.png" alt="img" /></p>
<ul>
<li><strong>match多个词的逻辑</strong></li>
</ul>
<p>上面等同于should（任意一个满足），是因为 match还有一个operator参数，默认是or, 所以对应的是should。</p>
<p>所以上述查询也等同于</p>
<pre><code class="language-bash">GET /test-dsl-match/_search
{
  &quot;query&quot;: {
    &quot;match&quot;: {
      &quot;title&quot;: {
        &quot;query&quot;: &quot;BROWN DOG&quot;,
        &quot;operator&quot;: &quot;or&quot;
      }
    }
  }
}
</code></pre>
<p>那么我们如果是需要and操作呢，即同时满足呢？</p>
<pre><code class="language-bash">GET /test-dsl-match/_search
{
  &quot;query&quot;: {
    &quot;match&quot;: {
      &quot;title&quot;: {
        &quot;query&quot;: &quot;BROWN DOG&quot;,
        &quot;operator&quot;: &quot;and&quot;
      }
    }
  }
}
</code></pre>
<p>等同于</p>
<pre><code class="language-bash">GET /test-dsl-match/_search
{
  &quot;query&quot;: {
    &quot;bool&quot;: {
      &quot;must&quot;: [
        {
          &quot;term&quot;: {
            &quot;title&quot;: &quot;brown&quot;
          }
        },
        {
          &quot;term&quot;: {
            &quot;title&quot;: &quot;dog&quot;
          }
        }
      ]
    }
  }
}
</code></pre>
<p><img src="assets/es-dsl-full-text-7.png" alt="img" /></p>
<h3>控制match的匹配精度</h3>
<p>如果用户给定 3 个查询词，想查找只包含其中 2 个的文档，该如何处理？将 operator 操作符参数设置成 and 或者 or 都是不合适的。</p>
<p>match 查询支持 minimum_should_match 最小匹配参数，这让我们可以指定必须匹配的词项数用来表示一个文档是否相关。我们可以将其设置为某个具体数字，更常用的做法是将其设置为一个百分数，因为我们无法控制用户搜索时输入的单词数量：</p>
<pre><code class="language-bash">GET /test-dsl-match/_search
{
  &quot;query&quot;: {
    &quot;match&quot;: {
      &quot;title&quot;: {
        &quot;query&quot;:                &quot;quick brown dog&quot;,
        &quot;minimum_should_match&quot;: &quot;75%&quot;
      }
    }
  }
}
</code></pre>
<p>当给定百分比的时候， minimum_should_match 会做合适的事情：在之前三词项的示例中， 75% 会自动被截断成 66.6% ，即三个里面两个词。无论这个值设置成什么，至少包含一个词项的文档才会被认为是匹配的。</p>
<p><img src="assets/es-dsl-full-text-8.png" alt="img" /></p>
<p>当然也等同于</p>
<pre><code class="language-bash">GET /test-dsl-match/_search
{
  &quot;query&quot;: {
    &quot;bool&quot;: {
      &quot;should&quot;: [
        { &quot;match&quot;: { &quot;title&quot;: &quot;quick&quot; }},
        { &quot;match&quot;: { &quot;title&quot;: &quot;brown&quot;   }},
        { &quot;match&quot;: { &quot;title&quot;: &quot;dog&quot;   }}
      ],
      &quot;minimum_should_match&quot;: 2 
    }
  }
}
</code></pre>
<p><img src="assets/es-dsl-full-text-9.png" alt="img" /></p>
<h3>其它match类型</h3>
<ul>
<li><strong>match_pharse</strong></li>
</ul>
<p>match_phrase在前文中我们已经有了解，我们再看下另外一个例子。</p>
<pre><code class="language-bash">GET /test-dsl-match/_search
{
  &quot;query&quot;: {
    &quot;match_phrase&quot;: {
      &quot;title&quot;: {
        &quot;query&quot;: &quot;quick brown&quot;
      }
    }
  }
}
</code></pre>
<p><img src="assets/es-dsl-full-text-11.png" alt="img" /></p>
<p>很多人对它仍然有误解的，比如如下例子：</p>
<pre><code class="language-bash">GET /test-dsl-match/_search
{
  &quot;query&quot;: {
    &quot;match_phrase&quot;: {
      &quot;title&quot;: {
        &quot;query&quot;: &quot;quick brown f&quot;
      }
    }
  }
}
</code></pre>
<p>这样的查询是查不出任何数据的，因为前文中我们知道了match本质上是对term组合，match_phrase本质是连续的term的查询，所以f并不是一个分词，不满足term查询，所以最终查不出任何内容了。</p>
<p><img src="assets/es-dsl-full-text-12.png" alt="img" /></p>
<ul>
<li><strong>match_pharse_prefix</strong></li>
</ul>
<p>那有没有可以查询出<code>quick brown f</code>的方式呢？ELasticSearch在match_phrase基础上提供了一种可以查最后一个词项是前缀的方法，这样就可以查询<code>quick brown f</code>了</p>
<pre><code class="language-bash">GET /test-dsl-match/_search
{
  &quot;query&quot;: {
    &quot;match_phrase_prefix&quot;: {
      &quot;title&quot;: {
        &quot;query&quot;: &quot;quick brown f&quot;
      }
    }
  }
}
</code></pre>
<p><img src="assets/es-dsl-full-text-13.png" alt="img" /></p>
<p>(ps: prefix的意思不是整个text的开始匹配，而是最后一个词项满足term的prefix查询而已)</p>
<ul>
<li><strong>match_bool_prefix</strong></li>
</ul>
<p>除了match_phrase_prefix，ElasticSearch还提供了match_bool_prefix查询</p>
<pre><code class="language-bash">GET /test-dsl-match/_search
{
  &quot;query&quot;: {
    &quot;match_bool_prefix&quot;: {
      &quot;title&quot;: {
        &quot;query&quot;: &quot;quick brown f&quot;
      }
    }
  }
}
</code></pre>
<p><img src="assets/es-dsl-full-text-14.png" alt="img" /></p>
<p>它们两种方式有啥区别呢？match_bool_prefix本质上可以转换为：</p>
<pre><code class="language-bash">GET /test-dsl-match/_search
{
  &quot;query&quot;: {
    &quot;bool&quot; : {
      &quot;should&quot;: [
        { &quot;term&quot;: { &quot;title&quot;: &quot;quick&quot; }},
        { &quot;term&quot;: { &quot;title&quot;: &quot;brown&quot; }},
        { &quot;prefix&quot;: { &quot;title&quot;: &quot;f&quot;}}
      ]
    }
  }
}
</code></pre>
<p>所以这样你就能理解，match_bool_prefix查询中的quick,brown,f是无序的。</p>
<ul>
<li><strong>multi_match</strong></li>
</ul>
<p>如果我们期望一次对多个字段查询，怎么办呢？ElasticSearch提供了multi_match查询的方式</p>
<pre><code class="language-bash">{
  &quot;query&quot;: {
    &quot;multi_match&quot; : {
      &quot;query&quot;:    &quot;Will Smith&quot;,
      &quot;fields&quot;: [ &quot;title&quot;, &quot;*_name&quot; ] 
    }
  }
}
</code></pre>
<p><code>*</code>表示前缀匹配字段。</p>
<h2>query string类型</h2>
<blockquote>
<p>第二类：query string 类型</p>
</blockquote>
<h3>query_string</h3>
<p>此查询使用语法根据运算符（例如AND或）来解析和拆分提供的查询字符串NOT。然后查询在返回匹配的文档之前独立分析每个拆分的文本。</p>
<p>可以使用该query_string查询创建一个复杂的搜索，其中包括通配符，跨多个字段的搜索等等。尽管用途广泛，但查询是严格的，如果查询字符串包含任何无效语法，则返回错误。</p>
<p>例如：</p>
<pre><code class="language-bash">GET /test-dsl-match/_search
{
  &quot;query&quot;: {
    &quot;query_string&quot;: {
      &quot;query&quot;: &quot;(lazy dog) OR (brown dog)&quot;,
      &quot;default_field&quot;: &quot;title&quot;
    }
  }
}
</code></pre>
<p>这里查询结果，你需要理解本质上查询这四个分词（term）or的结果而已，所以doc 3和4也在其中</p>
<p><img src="assets/es-dsl-full-text-15.png" alt="img" /></p>
<p>对构筑知识体系已经够了，但是它其实还有很多参数和用法，更多请参考<a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html">官网</a></p>
<h3>query_string_simple</h3>
<p>该查询使用一种简单的语法来解析提供的查询字符串并将其拆分为基于特殊运算符的术语。然后查询在返回匹配的文档之前独立分析每个术语。</p>
<p>尽管其语法比query_string查询更受限制 ，但<strong>simple_query_string 查询不会针对无效语法返回错误。而是，它将忽略查询字符串的任何无效部分</strong>。</p>
<p>举例：</p>
<pre><code class="language-bash">GET /test-dsl-match/_search
{
  &quot;query&quot;: {
    &quot;simple_query_string&quot; : {
        &quot;query&quot;: &quot;\&quot;over the\&quot; + (lazy | quick) + dog&quot;,
        &quot;fields&quot;: [&quot;title&quot;],
        &quot;default_operator&quot;: &quot;and&quot;
    }
  }
}
</code></pre>
<p><img src="assets/es-dsl-full-text-16.png" alt="img" /></p>
<p>更多请参考<a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-simple-query-string-query.html">官网</a></p>
<h2>Interval类型</h2>
<blockquote>
<p>第三类：interval类型</p>
</blockquote>
<p>Intervals是时间间隔的意思，本质上将多个规则按照顺序匹配。</p>
<p>比如：</p>
<pre><code class="language-bash">GET /test-dsl-match/_search
{
  &quot;query&quot;: {
    &quot;intervals&quot; : {
      &quot;title&quot; : {
        &quot;all_of&quot; : {
          &quot;ordered&quot; : true,
          &quot;intervals&quot; : [
            {
              &quot;match&quot; : {
                &quot;query&quot; : &quot;quick&quot;,
                &quot;max_gaps&quot; : 0,
                &quot;ordered&quot; : true
              }
            },
            {
              &quot;any_of&quot; : {
                &quot;intervals&quot; : [
                  { &quot;match&quot; : { &quot;query&quot; : &quot;jump over&quot; } },
                  { &quot;match&quot; : { &quot;query&quot; : &quot;quick dog&quot; } }
                ]
              }
            }
          ]
        }
      }
    }
  }
}
</code></pre>
<p><img src="assets/es-dsl-full-text-17.png" alt="img" /></p>
<p>因为interval之间是可以组合的，所以它可以表现的很复杂。更多请参考<a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-intervals-query.html">官网</a></p>
<h2>参考文章</h2>
<p>https://www.elastic.co/guide/en/elasticsearch/reference/current/full-text-queries.html#full-text-queries</p>
<p>https://www.elastic.co/guide/cn/elasticsearch/guide/current/match-multi-word.html</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="07&#32;查询：DSL查询之复合查询详解.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="09&#32;查询：DSL查询之Term详解.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434026dad870ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ElasticSearch%E7%9F%A5%E8%AF%86%E4%BD%93%E7%B3%BB%E8%AF%A6%E8%A7%A3/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
