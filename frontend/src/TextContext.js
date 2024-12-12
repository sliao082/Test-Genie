import React, { createContext, useState } from "react";

export const TextContext = createContext();

export const TextProvider = ({ children }) => {
    const [extractedText, setExtractedText] = useState("");
    const [lectureNotes, setLectureNotes] = useState("");
    const [summaryText, setSummaryText] = useState("");
    const [conversationHistory, setConversationHistory] = useState([]);

    return (
        <TextContext.Provider value={{
            extractedText, setExtractedText,
            lectureNotes, setLectureNotes,
            summaryText, setSummaryText,
            conversationHistory, setConversationHistory,
        }}>
            {children}
        </TextContext.Provider>
    );
};