'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  API: '"http:localhost/api"',
  module: {
    rules: [
      {
       test: /\.css$/,
       use: ['style-loader', 'css-loader'],
     }
   ]
  }
})