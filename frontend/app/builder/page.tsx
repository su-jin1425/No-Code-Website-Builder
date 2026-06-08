'use client';

import { useState } from 'react';
import { DndContext } from '@dnd-kit/core';

export default function BuilderPage() {
  const [components, setComponents] = useState([]);

  return (
    <div className="flex h-screen bg-zinc-950 text-white overflow-hidden">
      {/* Sidebar Component Library */}
      <aside className="w-64 border-r border-zinc-800 bg-zinc-900 p-4">
        <h2 className="text-xs font-bold uppercase text-zinc-500 mb-4">Components</h2>
        <div className="space-y-2">
          {['Hero', 'Text', 'Button', 'Image'].map(comp => (
            <div key={comp} className="p-3 bg-zinc-800 rounded cursor-move hover:bg-zinc-700 transition-colors">
              {comp}
            </div>
          ))}
        </div>
      </aside>

      {/* Main Canvas */}
      <main className="flex-1 p-8 bg-zinc-950 flex flex-col">
        <header className="flex justify-between items-center mb-6">
          <h1 className="text-xl font-bold">Project Name - Home</h1>
          <div className="space-x-3">
            <button className="px-4 py-2 bg-zinc-800 rounded hover:bg-zinc-700 text-sm">Preview</button>
            <button className="px-4 py-2 bg-blue-600 rounded hover:bg-blue-500 text-sm font-bold">Publish</button>
          </div>
        </header>

        <DndContext>
          <div className="flex-1 bg-white rounded-lg shadow-2xl border border-zinc-800 relative overflow-auto">
            {/* Canvas Area */}
            <div className="absolute inset-0 flex items-center justify-center text-zinc-400">
              Drag and drop components here
            </div>
          </div>
        </DndContext>
      </main>

      {/* Properties Panel */}
      <aside className="w-80 border-l border-zinc-800 bg-zinc-900 p-4">
        <h2 className="text-xs font-bold uppercase text-zinc-500 mb-4">Properties</h2>
        <div className="text-sm text-zinc-400 text-center mt-10">
          Select a component to edit its properties
        </div>
      </aside>
    </div>
  );
}
